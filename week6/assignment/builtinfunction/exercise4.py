import math
import time

def my4(n, ms):
    print(time.time())
    time.sleep(ms/1000)
    print(f'Square root of {n} after {ms} miliseconds {math.sqrt(n)}')
    print(time.time())

my4(25100, 2123)