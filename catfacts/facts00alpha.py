#!/usr/bin/env python3
""" AJRodriguez | Lab38a:PYthon, APIs, and JSON"""

# ipmorts the requests library
import requests

def main():
    # create r, which is our request object
    r = requests.get("http://cat-fact.herokuapp.com/facts")

    print(dir(r) )
main()
