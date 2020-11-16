import multiprocessing as mp

# define a example function
def Hello(pos,name):
    msg="Hello "+name
    output.put((pos, msg))

if __name__=="__main__":
    # Define an output queue
    output = mp.Queue()

    # Setup a list of processes that we want to run
    processes = [mp.Process(target=Hello, args=(x, "Gianluca")) for x in range(4)]

    # Run processes
    for p in processes:
        p.start()

    # Exit the completed processes
    for p in processes:
        p.join()
            
    # Get process results from the output queue
    results = [output.get() for p in processes]
            
    print(results)
