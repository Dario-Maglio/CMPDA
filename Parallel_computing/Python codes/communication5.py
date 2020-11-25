import multiprocessing 
import time

def sender(conn, msgs): 
    for msg in msgs:
        time.sleep(1) 
        conn.send(msg) 
        print("Sent the message: "+str(msg)) 

    conn.close() 

def receiver(conn): 
    time.sleep(2)
    while 1: 
        msg = conn.recv() 

        if msg == "END": 
            break
        print("Received the message: "+str(msg)) 

#MAIN
if __name__=="__main__":
    # messages to be sent 
    msgs = ["hello,", "how", "are you?", "END"] 
    # creating a pipe 
    parent_conn, child_conn = multiprocessing.Pipe() 
    
    # creating new processes 
    p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs)) 
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,)) 
    
    # running processes 
    p1.start() 
    p2.start() 
    # wait until processes finish 
    p1.join() 
    p2.join() 
