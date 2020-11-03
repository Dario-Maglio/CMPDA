import requests
import threading as thr
from time import perf_counter

buffer_size=1024

#define a function to manage the download
def download(url):
    response = requests.get(url, stream=True)
    filename = url.split("/")[-1]
    with open(filename,"wb") as f:
        for data in response.iter_content(buffer_size):
            f.write(data)

if __name__ == "__main__":            
    urls= [
        "http://cds.cern.ch/record/2690508/files/201909-262_01.jpg",
        "http://cds.cern.ch/record/2274473/files/05-07-2017_Calorimeters.jpg",
        "http://cds.cern.ch/record/2274473/files/08-07-2017_Spectrometer_magnet.jpg",
        "http://cds.cern.ch/record/2127067/files/_MG_3944.jpg",
        "http://cds.cern.ch/record/2274473/files/08-07-2017_Electronics.jpg",    
    ]

    t = perf_counter()
    
#sequential download    
    for url in urls:
        download(url)

    print("Time: "+str(perf_counter()-t))
