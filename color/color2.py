#!/usr/bin/env python3
""" AJRodriguez | Lab 33b: proper notation"""

## Installs the crayons package.
import crayons

def main():
    """Runtime code. Always indent a function"""
    # print 'red string' in red
    print(crayons.red('red string'))

    # Red White and Blue text
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.disable() # disables the crayons package
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.DISABLE_COLOR = False # enable the crayons package

    # This line will print in color because color is enabled
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    # print 'red string' in red and bold
    print(crayons.red('red string', bold=True))

    # print 'yellow string' in yellow and bold
    print(crayons.yellow('yellow string', bold=True))

    # print 'magenta string' in magenta and bold
    print(crayons.magenta('magenta string', bold=True))

    # print 'white string' in white and bold
    print(crayons.white('white string', bold=True))
    
    #print my name in green and yellow
    print(crayons.green('Anthony')), print(crayons.yellow('Rodriguez'))
# we must call our main function or our code will not run!
main()

