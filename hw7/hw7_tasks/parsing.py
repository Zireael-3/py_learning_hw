import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_exchange_rate():
    url = 'http://www.cbr.ru/development/sxml/'
    xml = await get_html(url)
    soup = BeautifulSoup(xml, 'xml')
    exchange_rate = soup.find('Valute', {'ID': 'R01235'}).Value.text
    return float(exchange_rate.replace(',', '.'))


async def get_company_info(url):
    html = await get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('h1', {'class': 'price-section__label'}).text.strip()
    code = soup.find('span', {'class': 'price-section__category'}).text.strip()
    price = soup.find('span', {'class': 'price-section__current-value'}).text.strip()
    pe_ratio = soup.find('div', {'class': 'snapshot__data-item snapshot__data-item--small'}).text.strip()
    growth = soup.find('td', {'class': 'table__td table__td--big positive'}).text.strip()
    low = soup.find('td', {'class': 'snapshot__data-item snapshot__data-item--small'}).text.strip()
    high = soup.find_all('td', {'class': 'snapshot__data-item snapshot__data-item--small'})[1].text.strip()
    return {
        'name': name,
        'code': code,
        'price': price,
        'pe_ratio': pe_ratio,
        'growth': growth,
        'low': low,
        'high': high
    }


async def get_sp500_companies():
    url = 'https://markets.businessinsider.com/index/components/s&p_500'
    html = await get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr', {'class': 'table__row'})
    companies = []
    for row in rows:
        link = row.find('a', {'class': 'table__link'})
        if link:
            url = 'https://markets.businessinsider.com' + link['href']
            company_info = await get_company_info(url)
            companies.append(company_info)
    return companies


async def save_top_companies(companies, key, filename):
    companies = sorted(companies, key=lambda x: x[key], reverse=True)[:10]
    with open(filename, 'w') as f:
        json.dump(companies, f, indent=4)


async def main():
    exchange_rate = await get_exchange_rate()
    companies = await get_sp500_companies()
    for company in companies:
        price = float(company['price'].replace(',', ''))
        company['price'] = round(price / exchange_rate, 2)
        pe_ratio = company['pe_ratio'].replace(',', '')
        if pe_ratio == 'N/A':
            company['pe_ratio'] = None
        else:
            company['pe_ratio'] = float(pe_ratio)
        growth = company['growth'].replace('%', '')
        company['growth'] = float(growth) if growth != 'N/A' else None
        low = float(company['low'].replace(',', ''))
        high = float(company['high'].replace(',', ''))
        potential_profit = round((high - low) / low * 100, 2)
        company['potential_profit'] = potential_profit
    await save_top_companies(companies, 'price', 'top_10_expensive_companies.json')
    await save_top_companies(companies, 'pe_ratio', 'top_10_low_pe_companies.json')
    await save_top_companies(companies, 'growth', 'top_10_growing_companies.json')
    await save_top_companies(companies, 'potential_profit', 'top_10_potential_profit_companies.json')

asyncio.run(main())
