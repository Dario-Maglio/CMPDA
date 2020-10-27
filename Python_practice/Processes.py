import multiprocessing as mp
import os

def hello(name):
    print(f"\n----> function {name}")
    print(f"Hello {name}")
    print(f"The number of the process is {str(os.getpid())}")
    print(f"The number of the father process is {str(os.getppid())}")

def f_name(name):
    print(f"\n----> function {name}")
    print(f"The number of the process is {str(os.getpid())}")
    print(f"The number of the father process is {str(os.getppid())}")


#MAIN
if __name__=="__main__":
    hello("Giovanni")
    process1 = mp.Process(target=hello, args=("Dario", ))
    process2 = mp.Process(target=f_name, args=("Cose", ))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    hello("Giorgio")
    #Questo stamperà cose un pò a caso
    Processes = mp.Pool(processes=4)
    results = Processes.map(f_name, range(1,10))
