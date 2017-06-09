#selling ticket system
#coding=utf8
import threading
import time
import os

def doChore():
    time.sleep(0.5)

def booth(tid):
    global i
    global lock
    while True:
        lock.acquire() #当多个线程修改同一个数值时，lock防止出错
        if i!=0:
            i=i-1
            print(tid,'now left:',i)
            doChore()
        else:
            print("Thread_id",tid,"No more tickets")
            os._exit(0)
        lock.release()
        doChore()

i=30
lock=threading.Lock()

for k in range(10):
    new_thread=threading.Thread(target=booth,args=(k,))
    new_thread.start()