#!/usr/bin/env python3

"""Author: Wes | Learning about Functions"""

import crayons

# functions that have one specific

def lab():
    """this function print a string in red"""
    # print 'red string' in red
    print(crayons.red('red string'))

    # Red White and Blue text
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.disable() # disables the crayons package
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.DISABLE_COLOR = False # enable the crayons package

    # This line will print in color because color is enabled
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

def lab2():
    """prints in red and bold"""
    # print 'red string' in red
    print(crayons.red('red string', bold=True))

    # print 'yellow string' in yellow
    print(crayons.yellow('yellow string', bold=True))

    # print 'magenta string' in magenta
    print(crayons.magenta('magenta string', bold=True))

    # print 'white string' in white
    print(crayons.white('white string', bold=True))

def lab3():
    """prints a name"""
    print(crayons.red('Wes', bold=True))


def main():
    lab2()
    lab()
    lab3()


if __name__ == "__main__":
    main()
