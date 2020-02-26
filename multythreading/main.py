import threading
import os
import time
current_dir = os.path.dirname(__file__)
def gender_filter(file_name, start_line,end_line):
    with open(os.path.join(current_dir,file_name),'r') as f:
        for line in f.readlines()[start_line:end_line]:
            info = line[:-1].split(",")
            if info[3] == 'male':
                with open(os.path.join(current_dir,"males.txt"),"a") as mFile:
                    mFile.write(line)
            elif info[3] == "female":
                with open(os.path.join(current_dir,"females.txt"),"a") as fFile:
                    fFile.write(line)
            time.sleep(0.1)

start_time = time.time()

#gender_filter("users.txt",50,100)
t1 = threading.Thread(target=gender_filter, args=("users.txt",1,33))
t2 = threading.Thread(target=gender_filter, args=("users.txt",33,66))
t3 = threading.Thread(target=gender_filter, args=("users.txt",66,100))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


print("Completion Time: ",time.time()-start_time)
            

