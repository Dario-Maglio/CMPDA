from multiprocessing import Process
import os
def f0(name):
    print()
    print("-----> function "+name)
    print ("I am still the main process with ID "
           +str(os.getpid())+" my father is ID:"+str(os.getppid()))

def f1(name):
    print()
    print("-----> function "+name)
    print ("I am the first sub-process with ID "
           +str(os.getpid())+" my father is ID:"+str(os.getppid()))
    f2('two')


def f2(name):
    print()
    print("-----> function "+name)
    print ("I am still the first sub-process with ID "
           +str(os.getpid())+" my father is ID:"+str(os.getppid()))
    print("This is the end!")

#MAIN
if __name__=="__main__":
    print ("I am the main process with ID: "+str(os.getpid()))
    f0('zero')
    p = Process(target=f1, args=('one',))
    p.start()
    p.join()
