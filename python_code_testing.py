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
import matplotlib
from matplotlib.pyplot import figure
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from textwrap import wrap
matplotlib.use('TkAgg')

switch = True
firststart = True

def draw_figure(canvas, figure):
    
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def calc_your_income(y, monthly_invest, interest_rate):

    if y.isnumeric() and monthly_invest.isnumeric() and interest_rate.isnumeric():
        fvar = calc_interest(y, monthly_invest, interest_rate)
        switch = True
        return fvar
    else:
        print("Nan")
        switch = False
        return switch, switch
    

def calc_interest(y, min, ira):

    qtest = 0
    rtest = 0
    rt = 12
    yt = rt / 12
    inv = []
    ninv = []
    totali = []
    totaln = []
    y = int(y)
    min = float(min)
    ira = (float(ira) + 100) / 100

    # y = 8
    # monthly_invest = 500
    # interest_rate = 1.05


    x_axis = list(range(1, y+1))
    for j in range(y):
        rt = (j + 1) * 12
        for i in range(rt):
            
            qtest = qtest + min
            rtest = rtest + min

            if (i+1) % 12 == 0:
                rtest = rtest * ira
                # print('iter no. ' + str(i) + ' : ' + str(rtest))

        print("Money gained without investing after " + str(rt/12) + " years: " + str(qtest-(min*12)*(j+1)))
        print("Money gained with    investing after " + str(rt/12) + " years: " + str(int(rtest-(min*12)*(j+1))))

        # data = "Money gained with    investing after " + str(rt/12) + " years: " + str(int(rtest-(min*12)*(j+1)))

        ninv.append(qtest-(min*12)*(j+1))
        inv.append(rtest-(min*12)*(j+1))
        totaln.append(qtest)
        totali.append(rtest)
        
        qtest = 0
        rtest = 0

    strings = ""
    for k in range(len(inv)):
        string = "Money gained with investing after {} years: {} € \n".format(k+1, int(inv[k]))
        strings += string

    data = strings
    # global firststart
    # if not firststart:
    #     ax1.cla()
    #     ax2.cla()
    fig, (ax1, ax2) = plt.subplots(2)
    fig.set_size_inches(6.75, 10)
    fig.savefig('test2png.png', bbox_inches='tight', dpi=100)
    longtitle = 'Money earned by investing {} per month for {} years with an {} % interest rate'.format(min, y, int((ira*100-100)))
    fig.suptitle("\n".join(wrap(longtitle, 50)))
    
    # figure(num=1, figsize=(10, 10), dpi=80)

    ax1.plot(x_axis, inv, label = "Investing Revenue")
    ax1.plot(x_axis, ninv, label = "Control Group")
    
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Amount')
    ax1.legend()
    
    # plt.plot(x_axis, rtest)
    
    # plt.figure(2)
    ax2.plot(x_axis, totaln, label = "Total Money Owned Without Investing")
    ax2.plot(x_axis, totali, label = "Total Money Owned With Investing")
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Amount')
    ax2.legend()
    # plt.plot(x_axis, rtest)
    # plt.show()
    firststart = False
    ircalc = plt.gcf()
    return ircalc, data

sg.theme('DarkBlue12')
# calc_your_income()
layout = [[sg.Text("xPara's Investing Calculator v1.0", font='Helvetica 15 bold'), sg.Text(size=(10,1), key='-OUTPUT-')],
          [sg.Text('Years Investing: ', size=(12,1)), sg.Input(key='-YEARS-')],
          [sg.Text('Monthly Amount: ', size=(12,1)), sg.Input(key='-MONTHLYI-')],
          [sg.Text('Interest Rate: ', size=(12,1)), sg.Input(key='-INTEREST-')],
          [sg.Text('', key='-WARNING-')],
          [sg.Button('Show'), sg.Button('Exit'), sg.Button('Reset')],
          [sg.Graph(50, 50, 50, key='-CANVAS-'), sg.vtop(sg.Multiline(size=(100,100), key='-MATH-', visible=False, font='Helvetica 11'))]]

# Create the window
window = sg.Window("INVESTING CALCULATOR", layout, size=(1200, 900))

# Create an event loop
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        
        
        window['-WARNING-'].update("Calculating...")
        funcvar, data = calc_your_income(values['-YEARS-'], values['-MONTHLYI-'], values['-INTEREST-'])
        if not funcvar:
            window['-WARNING-'].update("We serve food here, Sir. (Please enter numbers!)")
        else:
            window['-CANVAS-'].update(visible=True)
            if 'fig_canvas_agg' in locals():
                fig_canvas_agg.get_tk_widget().forget()
                plt.close('all')
            window['-MATH-'].update(visible=True)
            fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, funcvar)
            window['-MATH-'].update(data)
    if event == 'Reset':
        fig_canvas_agg._tkcanvas.delete("all")
        window['-MATH-'].update(visible=False)
        window['-CANVAS-'].update(visible=False)

window.close()