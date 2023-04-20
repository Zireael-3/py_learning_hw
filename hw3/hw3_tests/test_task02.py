import time
from multiprocessing import Pool
from hw3.hw3_tasks.task02 import slow_calculate


def test_slow_calculate():
    """testing that the code execution time does not exceed 1 minute"""
    with Pool(processes=25) as pool:
        start_time = time.time()
        results = pool.map(slow_calculate, range(501))
        end_time = time.time()
        total_time = end_time - start_time
        assert total_time < 60, 'The code execution took longer than 1 minute'
