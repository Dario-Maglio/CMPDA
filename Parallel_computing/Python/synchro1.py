import multiprocessing 

def withdraw(balance):	 
        for x in range(10000): 
                balance.value = balance.value-1
def deposit(balance):	 
	for x in range(10000): 
		balance.value = balance.value + 1

def perform_transactions(): 
	# initial balance (in shared memory) 
	balance = multiprocessing.Value('i', 100) 
	# creating new processes 
	p1 = multiprocessing.Process(target=withdraw, args=(balance,)) 
	p2 = multiprocessing.Process(target=deposit, args=(balance,)) 
	# starting processes 
	p1.start() 
	p2.start() 
	# wait until processes are finished 
	p1.join() 
	p2.join() 
	# print final balance 
	print("Final balance = {}".format(balance.value)) 

#MAIN
for x in range(10): 
    # perform same transaction process 10 times 
    perform_transactions() 
