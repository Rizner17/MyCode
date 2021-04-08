#!/usr/bin/env python3
""" AJRodriguez | Creating a graph with data from a weather API"""

# python3 -m pip install np
import numpy as np
# python3 -m pip install matplotlib
import matplotlib.pyplot as plt

def main():
    labels = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    week_temps = [85, 90, 81, 79, 80, 86, 91]
    width = 0.25       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, week_temps, width, label='Week') # shows the labels along the x-axis, takes the width from         above setting the bars to .25 width, dsisplays the week temperatures on the y-axis, and shows the label Week      above the bars.

    ax.set_ylabel('Temperature(Degrees)')#sets the y-axis as Temperature in degrees
    ax.set_title('Orlando Weekly Forecast')#sets the title as Orlando weekly forecast
    ax.legend()
    # plt.savefigure will save it in this directory as a pdf
    plt.savefig("/home/student/mycode/graphing/Orlandoforcast.pdf")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/Orlandoforcast.pdf")
    plt.show()
main()
