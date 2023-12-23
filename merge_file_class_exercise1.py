import time
import threading
import random

class file_writer(object):
    def __init__(self, file_name):
        self._file_name = file_name
        self._file = open(file_name, 'w')
        self.lock = threading.Lock()
        self.s = threading.Semaphore(3)

    def write_line(self, line):
        self.lock.acquire()
        self._file.write(line)
        self.lock.release()
    def read_line(self,line):
        self.s.acquire()
        self.lock.acquire()
        while(True):
            try:
                arr = self._file.readlines()
                print(arr[line-1])
                self.lock.release()
                self.s.release()
                return
            except:
                self.lock.release()
                self.s.release()
                time.sleep(0.1)
                self.s.acquire()
                self.lock.acquire()
            


def read_file_and_write_to_merged_file(file_path, merged_file):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            merged_file.write_line(line)
            time.sleep(0.1)
def read_file_to_merged_file(file_path, merged_file):
    with open(file_path, 'r') as file:
            line = random.randint(2,15)
            merged_file.read_line(line)
            time.sleep(0.1)






def merge_files(file1, file2, merged_file):
    thread1 = threading.Thread(target=read_file_and_write_to_merged_file, args=(file1,merged_file))
    thread2 = threading.Thread(target=read_file_and_write_to_merged_file, args=(file2,merged_file))
    throd1 = threading.Thread(target=read_file_to_merged_file, args=(file1,merged_file))
    throd2 = threading.Thread(target=read_file_to_merged_file, args=(file1,merged_file))
    thread1.start()
    thread2.start()
    throd1.start()
    throd2.start()
    thread1.join()
    thread2.join()
    throd1.join()
    throd2.join()

if __name__ == "__main__":
    file1 = r'C:\Alon\file1.txt'
    file2 = r'C:\Alon\file2.txt'
    my_file_writer = file_writer(r'C:\Alon\merged_file.txt')

    merge_files(file1, file2, my_file_writer)
