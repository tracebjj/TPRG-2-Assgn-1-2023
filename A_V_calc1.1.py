'''
TPRG 2131 Fall 2023 Assignment 1
October, 2023
Trace C <trace.carter@dcmail.ca>
'''
import math
from time import sleep

LEVELSELECTION = input("""A/V Calculator
 Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
 Enter V/v to change the calculated view or D/d for default view.
 """ ).lower()
if LEVELSELECTION == 'q':
    EQUATIONSELECT = input("""Select a function:
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation""")
elif LEVELSELECTION == 'v':
    EQUATIONSELECT = input("""Select a function:
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation""")