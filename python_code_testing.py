import datetime, time
import platform
import subprocess
from threading import Thread

def hosts():
    mylist = list(range(1, 51))
    for x in mylist:
        print("10.90.12." + str(x))

def compare_test():
    a = "abs"
    b = "abs"
    if not a is b:
        print('xti') 
    else:
        print('xtc')

def clock():
    while True:   
        now = datetime.now()
        # print (now.strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True),
        ticktack = now.strftime("%m/%d/%Y %H:%M:%S")
        # print("\r", end="", flush=True),
        time.sleep(1)
        return ticktack

# # - timedelta(days=1)  =   yesterday

import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    ping()
    # do your stuff
    sc.enter(5, 1, do_something, (sc,))


s.enter(5, 1, do_something, (s,))
# s.run()
print("test")


def ping():
    if platform.system() == "Windows":
        print("No Server Environment.")
    else:
        bashCommand = "sudo fping -s -g 10.90.12.1 10.90.12.50"
        
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        
ping()

if __name__ == '__main__':
    
    Thread(target = s.run()).start()
    