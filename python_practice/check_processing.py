import time
from multiprocessing import Pool


start_time = time.perf_counter()

def doSumInner(start, end):
    ts = 0
    for i in range(start, end):
        ts += i**2
    return ts

def doSumMultiProcess(n):
    cores = 5
    totalSum = 0
    iterables = [(i*n//cores, (i+1)*n//cores) for i in range(cores)]
    with Pool(cores) as pool:
        results = pool.starmap(doSumInner, iterables)
        print (results, type(results))
        totalSum = sum(results)
    return totalSum

def doSum(n):
    totalSum = 0
    for i in range(n):
        totalSum += i**2
    return totalSum

if __name__ == "__main__":
    n = 10**8
    # sum = doSum(n)
    sum = doSumMultiProcess(n)
    print (sum)
    end = time.perf_counter()
    elapsed_time = end - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")