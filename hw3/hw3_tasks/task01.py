from collections.abc import Callable


def cache(times):
    """parametrized decorator that accepts number of times to cache value"""
    caches = {'value': None, 'count': times}

    def caching_process(func):
        def wrapper(*args):
            if caches['count'] > 0 and caches.get('value'):
                caches['count'] -= 1
                return caches['value']
            else:
                caches['value'] = func(args)
                return caches['value']

        return wrapper

    return caching_process
