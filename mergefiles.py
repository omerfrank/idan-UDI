import threading
class FileWriter():
    def __init__(self, file):
        self.file = open(file,"w")
        self.canwrite = True
def read_file_and_write_to_merged_file(file_path, merged_file):
    for lines in file_path.readlines():
        while(merged_file.canwrite == False):
            {print("wait in line")}
        merged_file.canwrite = False
        merged_file.file.write(lines + "\n")
        merged_file.canwrite = True

def merge_files(file1, file2, merged_file):
    t1 = threading.Thread(target=read_file_and_write_to_merged_file(file_path=file1,merged_file=merged_file))
    t2 = threading.Thread(target=read_file_and_write_to_merged_file(file_path=file2,merged_file=merged_file))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print ("done")
merged = FileWriter(r"C:\Users\omerf\OneDrive\שולחן העבודה\tomer\idan&UDI\udiDone.txt")
merge_files(file1=open(r"C:\Users\omerf\OneDrive\שולחן העבודה\tomer\idan&UDI\udi1.txt","r"),file2=open(r"C:\Users\omerf\OneDrive\שולחן העבודה\tomer\idan&UDI\udi2.txt","r"),merged_file= merged)
