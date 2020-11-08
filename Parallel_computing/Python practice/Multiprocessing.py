"""Practice with the mp.Queue() and Pool()"""

import multiprocessing as mp
import os

# define a example function
def Hello(pos,name):
    msg = name
    output.put((pos, msg))

def cube(x):
    print ( "I am the first sub-process with ID "
        + str(os.getpid()) + ' my father is ID:' + str(os.getppid()))
    return x**3

if __name__=='__main__':
    # Define an output queue
    output = mp.Queue()
    # Setup a list of processes that we want to run
    processes = [mp.Process(target=Hello, args=(x, 'Gianluca')) for x in range(4)]
    # Run processes
    for p in processes:
        p.start()
    # Exit the completed processes
    for p in processes:
        p.join()
    # Get process results from the output queue
    results = [output.get() for p in processes]
    print(results)

    # Define a Pool, while .map execute and close the list of processes
    proc = mp.Pool(processes=7)
    results = proc.map(cube,range(1,20))
    print(results)

    pool = mp.Pool(processes=7)
    results = pool.map_async(cube,range(1,20))
    print(results.get())
