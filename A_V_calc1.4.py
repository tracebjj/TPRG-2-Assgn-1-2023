'''
TPRG 2131 Fall 2023 Assignment 1
October, 2023
Trace C <trace.carter@dcmail.ca>
'''
import math
from time import sleep

def FUNCTION_1(WIDTH, HEIGHT, LENGTH):
    print(WIDTH, HEIGHT, LENGTH)

VIEWSELECTION = input("""A/V Calculator
 Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
 Enter V/v to change the calculated view or D/d for default view.
 """ ).lower()

while True:
    EQUATIONSELECT = input("""Select a function:
    1.	Rectangular Prism Volume Calulation - V=whl
    2.	Rectangular Prism Area Calculation - A=2*(wl+hl+hw)
    3.	Circular Cone Volume Calculation - π(r^2)(h/3)
    4.	Circular Cone Area Calculation - πr[r+sqr(h^2+r^2)]
    5.	Sphere Volume Calculation - (4/3)πr^3
    6.	Sphere Area Calcultation - 4πr^2
    """)
    if EQUATIONSELECT== "1":
        print("Use the same units for all values:")
        WIDTH = input("What is the Width? " )
        HEIGHT = input("What is the Height? ")
        LENGTH = input("What is the Length? ")
        FUNCTION_1(WIDTH, HEIGHT, LENGTH)
    elif EQUATIONSELECT== "2":
        sleep(0.2)
    elif EQUATIONSELECT== "3":
        sleep(0.2)
    elif EQUATIONSELECT== "4":
        sleep(0.2)
    elif EQUATIONSELECT== "5":
        sleep(0.2)
    elif EQUATIONSELECT== "6":
        sleep(0.2)
    if VIEWSELECTION == 'q':
        sleep(0.1)
    elif VIEWSELECTION == 'v':
        print("")