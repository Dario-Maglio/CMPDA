import threading as thr
import requests
import os
from time import perf_counter

buffer_size=1024

#define a function to manage the download
def download(url):
    response = requests.get(url, stream=True)
    filename = url.split("/")[-1]
    with open(filename,"wb") as f:
        for data in response.iter_content(buffer_size):
            f.write(data)

#MAIN
if __name__ == "__main__":            
    urls= [
        "http://cds.cern.ch/record/2690508/files/201909-262_01.jpg",
        "http://cds.cern.ch/record/2274473/files/05-07-2017_Calorimeters.jpg",
        "http://cds.cern.ch/record/2274473/files/08-07-2017_Spectrometer_magnet.jpg",
        "http://cds.cern.ch/record/2127067/files/_MG_3944.jpg",
        "http://cds.cern.ch/record/2274473/files/08-07-2017_Electronics.jpg",    
    ]

#define 5 threads
    threads = [thr.Thread(target=download, args=(urls[x],)) for x in range(4)]

    t = perf_counter()

#start threads    
    for thread in threads:
        thread.start()

#join threads        
    for thread in threads:
        thread.join()


    print("Time: "+str(perf_counter()-t))
