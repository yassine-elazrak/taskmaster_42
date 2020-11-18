
import threading
import os
import time
from  subprocess import Popen , PIPE
from threading import Timer
import threading
global list_pid
list_pid = []

def my_job(pill_name):
    fd=open("out",'w')
    process = Popen(["ls" ,"-la"], stdout=fd, stderr=PIPE)
    stdout, stderr = process.communicate()
    print("It's time to take your pill " + pill_name + "pid=" + str(process.pid))
    list_pid.append(process.pid)

# t1=threading.Thread(target=my_job, args=["advil"])
# t1.start()
# t2=threading.Thread(target=my_job, args=["tylenol"])
# t2.start()
# t3=threading.Thread(target=my_job, args=["motrin"])
# t3.start()

# def task():
#     time.sleep(0.9)
#     print("hello yassine")
#     for pid in list_pid:
#         print ("pid_= {}".format(pid))
# t4=threading.Thread(target=task)
# t4=threading.Thread(target=task)
# t4.start()
#Timer(3,my_job,["yassine"]).start()
# print(dir(threading))

import signal, os

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")


import os
import subprocess

#os.chdir("/tmp/")
#3p=os.getcwd()
#print("\n",p)

from threading import Thread
from time import sleep
import sys

def timer():
    for i in range(45):
        sleep(10)
        print("sleep=",i)
        #waits 45 seconds
    sys.exit() #stops program after timer runs out, you could also have it print something or keep the user from attempting to answer any longer

def question():
    answer = input("foo?")
    print("answer=", answer)

t1 = Thread(target=timer)
t2 = Thread(target=question)
t1.start() #Calls first function
t2.start() #Calls second function to run at same time





