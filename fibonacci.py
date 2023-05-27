import numpy as np
import matplotlib.pyplot as plt
import time
from decimal import *
getcontext().prec = 2000

values = np.array([i for i in range(10001)])
times = []

def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def faster_fibonacci(n):
    prev_previous, previous, current = 0, 0, 1
    
    for i in range(n + 1):
        prev_previous = previous
        previous = current
        current = prev_previous + previous
            
    return current
    
def fastest_fibonacci(n):
    return ((((((1 + Decimal(5).sqrt()) / Decimal(5).sqrt())) ** n) - (((1 - Decimal(5).sqrt()) / Decimal(5).sqrt())) ** n)) / 2

def benchmark(fn, n):
    start = time.time()
    for i in range(n + 1):
        fn(i)
        times.append(time.time() - start)
        
        
benchmark(fastest_fibonacci, 10000)
plt.plot(values, times)
plt.show()
