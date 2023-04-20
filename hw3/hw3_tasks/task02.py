import time
import struct
import random
import hashlib
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


if __name__ == '__main__':
    """
        To fix the error "An attempt has been made to start a new process before the current process has finished its 
        bootstrapping phase." I used this proper idiom in the main module
    """
    with Pool(processes=25) as pool:
        """
            25 processes is enough to keep within 60 seconds
        """
        results = pool.map(slow_calculate, range(501))
        total_sum = sum(results)
        print(total_sum)
