#!/usr/bin/env python
import pyMenu
ans = input('Start conversions?(y/n) :')
x = pyMenu.menu_handler()

if ans == 'y':
        print('Opening menu...')
        exec(open('pyMenu.py').read())
else:
    print('Closing menu...')
    exit()



#def create_menu(ans):

#def menuItems():
