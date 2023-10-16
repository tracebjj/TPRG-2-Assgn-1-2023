'''
TPRG 2131 Fall 2023 Assignment 1
October, 2023
Trace C <trace.carter@dcmail.ca>
'''
import math
from time import sleep

def FUNCTION_1(WIDTH, HEIGHT, LENGTH): #Rectangular Prism Volume Calculator
    return WIDTH*HEIGHT*LENGTH
    # Checks which view selection they chose
            
VIEWSELECTION = input("""A/V Calculator
 Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
 Enter V/v to change the calculated view or D/d for default view.
 """ ).lower()
if VIEWSELECTION == "q": # Checks for quit
    print("Thank you!")
    sleep(0.5)
    print("Goodbye!")
    sleep(1)
    exit()
while True: # Enters the main calculator loop
    # Asks which calculation they would like to perform
    EQUATIONSELECT = input("""Select a function (enter q to quit):
    1.	Rectangular Prism Volume Calulation - V=whl
    2.	Rectangular Prism Area Calculation - A=2*(wl+hl+hw)
    3.	Circular Cone Volume Calculation - π(r^2)(h/3)
    4.	Circular Cone Area Calculation - πr[r+sqr(h^2+r^2)]
    5.	Sphere Volume Calculation - (4/3)πr^3
    6.	Sphere Area Calcultation - 4πr^2
    """)
    # Checks which calculation they selected
    if EQUATIONSELECT== "1":
        print("Use the same units for all values:")
        WIDTH = int(input("What is the Width? " ))
        HEIGHT = int(input("What is the Height? "))
        LENGTH = int(input("What is the Length? "))
        
        if VIEWSELECTION == 'd':
            print(WIDTH,"×", HEIGHT,"×", LENGTH, "=", FUNCTION_1(WIDTH, HEIGHT, LENGTH))
            sleep(1)
        elif VIEWSELECTION == 'v':
            print(WIDTH,"×", HEIGHT,"×", LENGTH, "=", FUNCTION_1(WIDTH, HEIGHT, LENGTH), " | whl=V")
            sleep(2)

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
    elif EQUATIONSELECT == "q": # Checks for quit again
        print("Thank you!")
        sleep(0.5)
        print("Goodbye!")
        sleep(1)
        exit()
