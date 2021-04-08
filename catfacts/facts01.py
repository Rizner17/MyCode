#!/usr/bin/env python3
""" AJRodriguez | Lab38b: Python, APIs printing a JSON file"""

# imports the requests library
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    print(r.json())
main()

