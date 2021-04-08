#!/usr/bin/env python3
""" AJRodriguez | API import practice to use in mygraph.py"""

# import requests library
import requests

def main():
    """Requests API from source"""
    # create r, which is our request object
    Forecast = requests.get("https://api.weatherbit.io/v2.0/forecast/3hourly?city_id=Orlando&units=I&key=e12803af5f5a43ec9f72b2e4d4ae6f53")
    # display the methods available to our new object
    print(Forecast.json())
main()

