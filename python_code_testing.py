# import datetime, time
# import platform
# import subprocess
# from threading import Thread
# from flask import Flask

# app = Flask(__name__)

# def hosts():
#     mylist = list(range(1, 51))
#     for x in mylist:
#         print("10.90.12." + str(x))

# def compare_test():
#     a = "abs"
#     b = "abs"
#     if not a is b:
#         print('xti') 
#     else:
#         print('xtc')



# def clock():
#     while True:   
#         now = datetime.now()
#         # print (now.strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True),
#         ticktack = now.strftime("%m/%d/%Y %H:%M:%S")
#         # print("\r", end="", flush=True),
#         time.sleep(1)
#         return ticktack

# # - timedelta(days=1)  =   yesterday

# import sched, time
# s = sched.scheduler(time.time, time.sleep)
# def ping_daily(sc): 
#     ping()
#     # do your stuff
#     sc.enter(5, 1, ping_daily, (sc,))


# s.enter(5, 1, ping_daily, (s,))
# s.run()


# def ping():
#     if platform.system() == "Windows":
#         print("No Server Environment.")
#     else:
#         bashCommand = "sudo fping -s -g 10.90.12.1 10.90.12.50"
        
#         process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#         output, error = process.communicate()
        
# # ping()

# import time
# import atexit
# from datetime import datetime, timedelta
# from apscheduler.schedulers.background import BackgroundScheduler


# print("test_1")
# atm = datetime.now() + timedelta(seconds=30)
# def print_date_time(text):
#     print(text, time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

# scheduler = BackgroundScheduler()
# scheduler.add_job(func=print_date_time, trigger="date", run_date=atm, args=['Job execution start: '])
# scheduler.add_job(func=print_date_time, trigger="interval", seconds=2, args=["The current time is: "])
# scheduler.start()


# print(atm)
# Shut down the scheduler when exiting the app
# atexit.register(lambda: scheduler.shutdown())

# if __name__ == '__main__':
#     app.run()

# from typing import final


# years = 15
# principal = 0
# month_i = 50
# interest = 0.05 / 12

# years = years * 12
# # month_i = month_i * 12

# final_amount = 0

# for i in range(0, years):
#     if final_amount == 0:
#         final_amount = principal
    
#     final_amount = (final_amount + month_i) * (1 + interest)
    

# print('interest: ' + str(final_amount))
# print('no interest: ' + str(no_interest))

import matplotlib.pyplot as plt





# def customize():
#     y = input("Years: ")
#     monthly_invest = input("Investing per month: ")
#     interest_rate = input("Interest (default 5%): ")

def calc_interest():

    qtest = 0
    rtest = 0
    rt = 12
    yt = rt / 12
    inv = []
    ninv = []
    totali = []
    totaln = []

    y = 8
    monthly_invest = 500
    interest_rate = 1.05


    x_axis = list(range(1, y+1))
    for j in range(y):
        rt = (j + 1) * 12
        for i in range(rt):
            
            qtest = qtest + monthly_invest
            rtest = rtest + monthly_invest

            if (i+1) % 12 == 0:
                rtest = rtest * interest_rate
                # print('iter no. ' + str(i) + ' : ' + str(rtest))


        print("Money gained without investing after " + str(rt/12) + " years: " + str(qtest-6000*(j+1)))
        print("Money gained with    investing after " + str(rt/12) + " years: " + str(int(rtest-6000*(j+1))))
        ninv.append(qtest-6000*(j+1))
        inv.append(rtest-6000*(j+1))
        totaln.append(qtest)
        totali.append(rtest)
        
        qtest = 0
        rtest = 0

    plt.plot(x_axis, inv, label = "Investing Revenue")
    plt.plot(x_axis, ninv, label = "Control Group")
    plt.xlabel('Years')
    plt.ylabel('Money')
    plt.legend()
    # plt.plot(x_axis, rtest)
    plt.show()

    plt.plot(x_axis, totaln, label = "Total Money Owned Without Investing")
    plt.plot(x_axis, totali, label = "Total Money Owned With Investing")
    plt.xlabel('Years')
    plt.ylabel('Money')
    plt.legend()
    # plt.plot(x_axis, rtest)
    plt.show()

calc_interest()