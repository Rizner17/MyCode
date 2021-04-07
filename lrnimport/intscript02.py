#!/usr/bin/env python3
""" AJRodriguez | Lab34b: scripting, but with the entire subprocess lib"""

#imports the entire subprocess library
import subprocess

def main():
    subprocess.call(["ip", "link", "show", "up"])
    print("This program will check your interfaces.")
    interface = input("Enter an interface, like, ens3: ")
    subprocess.call(["ip", "addr", "show", "dev", interface])
    subprocess.call(["ip", "route", "show", "dev", interface])
# cannot use just call since the entire library was imported, must specify command

main()
