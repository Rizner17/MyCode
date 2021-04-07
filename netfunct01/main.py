#!/usr/bin/env python3
"""AJRodriguez | multifunction lab with colors"""
import crayons #imports crayon library to change the color of words

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    """define commandpush function"""
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print(crayons.green('Attempting to sending command --> ' + mycmds ))
            # we'll learn to write code that sends cmds to device here
#Reboot function
def reboot(devicecmd):
    """define the reboot function"""
    for ip in devicecmd.keys():
        print(crayons.yellow('Connecting to...' + ip )) # prints in yellow (...)
# start our main script
def main():
    """this function will recall the above functions"""
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    # data that replaces data stored in file
    print(crayons.blue("Welcome to the network device command pusher")) # welcome message
    ## get data set
    print(crayons.magenta("\nData set found\n"))
    ## run
    commandpush(work2do) # call function to push commands to devices
    reboot(work2do)
# call our main function
main()
