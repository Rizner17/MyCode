#!/usr/bin/env python3
""" AJRodriguez | lab24b: reading across a .txt file and looping"""

# open file in read mode
dnsfile = open("dnsservers.txt", "r")

# create list of lines
dnslist = dnsfile.readlines()

# loop over lines
for svr in dnslist:
    #print and end without a newline
    print(svr, end="")

# close your file
dnsfile.close()

