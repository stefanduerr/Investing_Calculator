import math, random
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg


class Canvas(FigureCanvasTkAgg):
    """
    Create a canvas for matplotlib pyplot under tkinter/PySimpleGUI canvas
    """
    def __init__(self, figure=None, master=None):
        super().__init__(figure=figure, master=master)
        self.canvas = self.get_tk_widget()
        self.canvas.pack(side='top', fill='both', expand=1)

# 1. Select the backend TkAgg for rendering to a tkinter canvas
matplotlib.use('TkAgg')

# 2. create PySimpleGUI window
font = ("Courier New", 11)
sg.theme("DarkBlue3")
sg.set_options(font=font)
layout = [
    [sg.Input(expand_x=True, key='Path'),
     sg.FileBrowse(file_types=(("ALL CSV Files", "*.csv"), ("ALL Files", "*.*"))),
     sg.Button('Plot')],
    [sg.Graph((640, 480), (0, 0), (640, 480), background_color='green', key='Graph')],
    [sg.Push(), sg.Button('Exit')]
]
window = sg.Window('Matplotlib', layout, finalize=True)

# 3. Create a matplotlib canvas under sg.Canvas or sg.Graph
fig, ax = plt.subplots()
sg_canvas = window['Graph'].Widget
canvas = Canvas(fig, sg_canvas)

# 4. initial for figure
ax.set_title(f"Sensor Data")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_xlim(0, 1079)
ax.set_ylim(-1.1, 1.1)
ax.grid()
canvas.draw()                       # do Update to GUI canvas

# 5. PySimpleGUI event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event == 'Plot':
        """
        path = values['Path']
        if not Path(path).is_file():
            continue
        """
        # 6. Get data from path and plot from here
        ax.cla()                    # Clear axes first if required
        ax.set_title(f"Sensor Data")
        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        ax.grid()
        theta = random.randint(0, 359)
        x = [degree for degree in range(1080)]
        y = [math.sin((degree+theta)/180*math.pi) for degree in range(1080)]
        plt.plot(x, y)
        canvas.draw()               # do Update to GUI canvas

# 7. Close window to exit
window.close()