#!/usr/bin/env python3
""" AJRodriguez | Lab 27a: Writing to files"""

# opens file admin.rc in append (a) mode to add to the file
outFile = open("admin.rc", "a")
# designates user input to the question "what tis the OS auth url"
osAUTH = input("What is the OS_AUTH_URL?")
print("export OS_AUTH_URL=" + osAUTH, file=outFile)

print("export OS_IDENTITY_API_VERSION=3", file=outFile)
# designates user input to the question 
osPROJ = input("What is the OS_PROJECT_NAME?")
print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)
# designates user input to the question
osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME?")
print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)
# designates user input to the question
osUSER = input("What is the OS_USERNAME?")
print("export OS_USERNAME=" + osUSER, file=outFile)
# designates user input to the question
osUSERDOM = input("What is the OS_USER_DOMAIN_NAME?")
print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)
# designates user input to the question
osPASS = input("What is the OS_PASSWORD?")
print("export OS_PASSWORD=" + osPASS, file=outFile)
outFile.close()
