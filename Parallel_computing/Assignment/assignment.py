"""Assignment: parallel programming."""

import argparse
import logging
import time
from functools import wraps
import matplotlib.pyplot as plt
import multiprocessing as mlp
import threading as mlt
import numpy


def clocked(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global  elapsed_times
        tstart = time.time()
        result = func(*args, **kwargs)
        exec_time = time.time() - tstart
        logger.info(f'Function {func.__name__} executed in {exec_time} s\n')
        elapsed_times.append(exec_time)
        return result
    return wrapper


@clocked
def serial_sum(nums):
    a = 1
    outlist = []
    primes_sum = 0
    for val in nums:
        primes_sum += sum_primes([a, val])
        outlist.append([val, primes_sum])
        a = val
    return outlist


@clocked
def mlp_sum(nums, N):
    sum = 0
    outlist = []
    processes = mlp.Pool(processes=N)
    entries = [[1, nums[0]]]
    for i in range(len(nums)-1):
        entries.append([nums[i], nums[i+1]])

    results = processes.map(sum_primes,entries)

    for i in range(len(nums)):
        sum += results[i]
        outlist.append([nums[i], sum])
    return outlist


@clocked
def mlt_sum(nums, n):
    sum = 0
    global outlist
    entries = [[1, nums[0]]]
    for i in range(len(nums)-1):
        entries.append([nums[i], nums[i+1]])

    threads = [mlt.Thread(target=sum_primes_mlt, args=(entries[i], )) for i in range(len(nums))]
    for thr in threads:
        thr.start()
    for thr in threads:
        thr.join()

    for i in range(len(nums)):
        sum += outlist[i]
        outlist[i] = [nums[i], sum]


def sum_primes_mlt(items):
    """Sums the prime numbers in the intervall between a and b for mlt_sum.
    """
    a, b = items
    sum = 0
    if a < b: #if a == b return zero
        while a < b :
            if is_a_prime(a):
                sum += a
            a += 1
    outlist.append(sum)


def sum_primes(items):
    """Sums the prime numbers in the intervall between a and b, including a.
    """
    a, b = items
    sum = 0
    if a < b: #if a == b return zero
        while a < b :
            if is_a_prime(a):
                sum += a
            a += 1
    return sum


def is_a_prime(num):
    """ Store True for prime numbers and False otherwise using a naive
        factorization method. It takes an integer 'n', creates a list
        of its factors and it veryfies if 'n' is a prime.
    """
    p = 2
    n = num
    factors = []

    while True:
        if n == 1:
            break
        r = n % p
        if r == 0:
            factors.append(p)
            n = n // p
        elif p * p >= n:
            factors.append(n)
            break
        elif p > 2:
            p += 2
        else:
            p += 1

    if (factors == [num]) or (num == 1):
        return True
    else:
        return False


#-------------------------------------------------------------------------------

def plot_results(elapsed, labels):
    plt.rcdefaults()
    fig, ax = plt.subplots()
    laby = tuple(i for i in labels)
    y_pos = numpy.arange(len(laby))
    ax.barh(y_pos, elapsed, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(laby)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Elapsed time')
    ax.set_title('Serial, threads & processes comparison')
    plt.show()

#------------------------------------------------------------------------------

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-v', '--verbose', action='store_true', help='DEBUG')
    ARGS = PARSER.parse_args()

    logger = logging.getLogger("LocalLog")
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if ARGS.verbose:
        logger.basicConfig(level=logging.DEBUG)
        logger.info('Logging level set on DEBUG.')

    N = 9
    elapsed_times = []     # Global elapsed_times list to wrap functions
    labels = ['Serial']    # Labels for the plot
    nums = range(100000, 2500000, 100000)

    assert nums[0] >= 1
    assert N//3 > 0

    print('\nThe list of the numbers is:\n', list(nums))
    print('#-----------------------------------------------------------------#')
    print('\nSerial execution.')
    print('Output from the serial method:\n', serial_sum(nums))
    print('#-----------------------------------------------------------------#')
    for n in range(2, N, N//3):
        labels.append(f'Multiprocess {n}')
        print(f'\nExecution with {n} processes.')
        print('Output from the multiprocessing method:\n', mlp_sum(nums, n))
    print('#-----------------------------------------------------------------#')
    for n in range(2, N, N//3):
        labels.append(f'Threads {n}')
        print(f'\nExecution with {n} threads.')
        outlist = []
        mlt_sum(nums, n)
        print('Output from the multithreading method:\n', outlist)
    print('#-----------------------------------------------------------------#')

    logger.info(elapsed_times)
    plot_results(elapsed_times, labels)
    print('The work is done.')
