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

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def calc_your_income(y, monthly_invest, interest_rate):

    if y.isnumeric() and isfloat(monthly_invest) and isfloat(interest_rate):
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

        print("Money gained without investing after " + str(rt/12) + " years: " + str(round(qtest, 2)))
        print("Money gained with    investing after " + str(rt/12) + " years: " + str(float(rtest-(min*12)*(j+1))))
        test = 1.234223
        print(round(test, 2))

        # data = "Money gained with    investing after " + str(rt/12) + " years: " + str(int(rtest-(min*12)*(j+1)))

        ninv.append(qtest-(min*12)*(j+1))
        inv.append(rtest-(min*12)*(j+1))
        totaln.append(qtest)
        totali.append(rtest)
        
        qtest = 0
        rtest = 0

    strings = ""
    years_amount = []

    big_numbers = [
        [4, "Thousand €"],
        [7, "Million €"],
        [10, "Billion €"],
        [13, "Trillion €"],
        [16, "Quadrillion €"],
        [19, "Quintillion €"],
        [22, "Sextillion €"],
        [25, "Septillion €"],
        [28, "Octillion €"],
        [31, "Nonillion €"],
        [34, "Decillion €"]        
    ]

    print('{:,}'.format(round(totali[0]), 2))
    for k in range(len(inv)):
        
        #     years_amount.append([k+1, str('{:,}'.format(round(totaln[k]), 2)) + ' €', str('{:,}'.format(round(totali[k]/1000000), 2)) + ' Mia. €', str('{:,}'.format(round(inv[k]), 2)) + ' €'])
        # else:
 
        value = int(totali[k])
        print('val: ' + str(value))
        num = len(str(value))
        for i in range(len(big_numbers)):
            # print('unformatted: ' + str(value))
            if big_numbers[i][0] <= num and num - big_numbers[i][0] < 3:
                # print(str(num) + ' ' + str(big_numbers[i][0]))
                frm = int('1' + (big_numbers[i][0]-1) * '0')
                print(str(round(value/frm, 2)) + ' ' + str(big_numbers[i][1]))


        years_amount.append([k+1, str('{:,}'.format(round(totaln[k]), 2)) + ' €', str('{:,}'.format(round(totali[k]), 2)) + ' €', str('{:,}'.format(round(inv[k]), 2)) + ' €'])
        string = "Money gained with investing after {} years: {} € \n".format(k+1, round(inv[k]))
        strings += string

    data = years_amount
    # global firststart
    # if not firststart:
    #     ax1.cla()
    #     ax2.cla()
    fig, (ax1, ax2) = plt.subplots(2)
    fig.set_size_inches(6.75, 10)
    fig.savefig('test2png.png', bbox_inches='tight', dpi=100)
    longtitle = 'Money earned by investing {} per month for {} years with a {} % interest rate'.format(min, y, round(ira*100-100, 2))
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

# sg.vtop(sg.Multiline(size=(10,10), key='-MATH-', visible=False, font='Helvetica 11')),
sg.theme('DarkBlue12')
testlist = [[1,2,3,4],[1,3,4,5]]
headings = ['Years', 'Wealth Without Investing', 'Wealth With Investing', 'Revenue By Investing']
layout = [[sg.Text("xPara's Investing Calculator v1.0", font='Helvetica 15 bold'), sg.Text(size=(10,1), key='-OUTPUT-')],
          [sg.Text('Years Investing: ', size=(12,1)), sg.Input(key='-YEARS-')],
          [sg.Text('Monthly Amount: ', size=(12,1)), sg.Input(key='-MONTHLYI-')],
          [sg.Text('Interest Rate: ', size=(12,1)), sg.Input(key='-INTEREST-')],
          [sg.Text('', key='-WARNING-')],
          [sg.Button('Show'), sg.Button('Exit'), sg.Button('Reset')],
          [sg.vtop(sg.Graph(50, 50, 50, key='-CANVAS-')), 
          sg.vtop(sg.Table(values=testlist,
        headings=headings, 
        def_col_width=20,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    justification='center',
                    num_rows=100,
                    col_widths=[7,17,15,15],
                    key='-TABLE-',
                    row_height=20,
                    visible=False))]
          ]

# Create the window
window = sg.Window("INVESTING CALCULATOR", layout, size=(1220, 900))

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
            
            fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, funcvar)
            
            window['-TABLE-'].update(visible=True)# window['-MATH-'].update(data)
            window['-TABLE-'].update(data)
    if event == 'Reset':
        window['-CANVAS-'].update(visible=False)
        window['-TABLE-'].update(visible=False)
        if 'fig_canvas_agg' in locals():
            fig_canvas_agg.get_tk_widget().forget()
            plt.close('all')
        

window.close()