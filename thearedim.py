import threading
import time
import urllib.request

def read_url(url_path):
    i = urllib.request.urlopen(url_path).read() 
    print(f"{i}")

def movie(num):
    print(read_url(num))
arr = []
n = time.time()
for i in range(32):
    t1 = threading.Thread(group=None,target=movie, args=[f"https://data.cyber.org.il/os/demo/movie{i+1}.txt"])
    t1.start()
    arr.append(t1)
for i in arr:
    i.join()
n -=time.time() 
z = time.time()
for i in range(32):
    movie(f"https://data.cyber.org.il/os/demo/movie{i+1}.txt")
print(n-(z-time.time()))


