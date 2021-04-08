#!/usr/bin/env python3
""" AJRodriguez | Creating a graph with data from a weather API"""

# python3 -m pip install np
import numpy as np
# python3 -m pip install matplotlib
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

def main():
    labels = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    week_temps = [85, 90, 81, 79, 80, 86, 91]
    width = 0.25       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, week_temps, width, label='Week')

    ax.set_ylabel('Temperature(Degrees)')
    ax.set_title('Orlando Weekly Forecast')
    ax.legend()
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    plt.savefig("/home/student/mycode/graphing/Orlandoforcast.pdf")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/Orlandoforcast.pdf")
    plt.show()
main()
