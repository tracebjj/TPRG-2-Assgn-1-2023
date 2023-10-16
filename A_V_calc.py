'''
TPRG 2131 Fall 2023 Assignment 1
October, 2023
Trace C <trace.carter@dcmail.ca>
'''
import math
from time import sleep

def FUNCTION_1(WIDTH, HEIGHT, LENGTH): #Rectangular Prism Volume Calculator
    return WIDTH*HEIGHT*LENGTH
def FUNCTION_2(WIDTH, HEIGHT, LENGTH): #A=2*(wl+hl+hw)
    WL = WIDTH*LENGTH
    HL = HEIGHT*LENGTH
    HW = HEIGHT*WIDTH
    BRACKETS = WL+HL+HW
    return 2*BRACKETS
     
def FUNCTION_3(RADIUS,HEIGHT):  #functions for the circular cone calculations
    R2 = RADIUS**2
    PI = math.pi
    return PI*(R2)*(HEIGHT/3)
def FUNCTION_4(RADIUS, HEIGHT):
    PIR = math.pi*RADIUS
    BRACKETSH = HEIGHT**2
    BRACKETSR = RADIUS**2
    RH = BRACKETSH + BRACKETSR
    return PIR*(RADIUS+math.sqrt(RH))

def FUNCTION_5(RADIUS): #(4/3)πr^3
    return (4/3)*math.pi*(RADIUS**3)
def FUNCTION_6(RADIUS): #4πr^2
    return 4*(math.pi)*(RADIUS**2)
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
        # Checks which view selection they chose
        if VIEWSELECTION == 'd':
            print(WIDTH,"×", HEIGHT,"×", LENGTH, "=", FUNCTION_1(WIDTH, HEIGHT, LENGTH))
            sleep(1)
        elif VIEWSELECTION == 'v':
            print(WIDTH,"×", HEIGHT,"×", LENGTH, "=", FUNCTION_1(WIDTH, HEIGHT, LENGTH), " | whl=V")
            sleep(2)

    elif EQUATIONSELECT== "2":
        print("Use the same units for all values:")
        WIDTH = int(input("What is the Width? " ))
        HEIGHT = int(input("What is the Height? "))
        LENGTH = int(input("What is the Length? "))
        if VIEWSELECTION == 'd':
            print(WIDTH,"×", HEIGHT,"×", LENGTH, "=", FUNCTION_2(WIDTH, HEIGHT, LENGTH))
            sleep(1)
        elif VIEWSELECTION == 'v':
            print("2","×","[(",WIDTH,")(",LENGTH,")+(",HEIGHT,")(",LENGTH,")+(",HEIGHT,")(",WIDTH,")]","=", FUNCTION_2(WIDTH,HEIGHT,LENGTH)," | 2*(wl+hl+hw)=A")
            sleep(2)

    elif EQUATIONSELECT== "3":
        RADIUS = int(input("What is the Radius? " ))
        HEIGHT = int(input("What is the Height? " ))
        if VIEWSELECTION == 'd':
            print("π(",RADIUS,"^2)(",HEIGHT,"/3)","=", FUNCTION_3(RADIUS, HEIGHT))
        elif VIEWSELECTION == 'v':
            print("π(",RADIUS,"^2)(",HEIGHT,"/3)","=", FUNCTION_3(RADIUS, HEIGHT)," | π(r^2)(h/3)")

    elif EQUATIONSELECT== "4":
        RADIUS = int(input("What is the Radius? " ))
        HEIGHT = int(input("What is the Height? " ))
        if VIEWSELECTION == 'd':
            print("π×",RADIUS,"×[",RADIUS,"+sqr(",HEIGHT,"^2+",RADIUS,"^2)","=", FUNCTION_4(RADIUS, HEIGHT))
        if VIEWSELECTION == 'v':
            print("π×",RADIUS,"×[",RADIUS,"+sqr(",HEIGHT,"^2+",RADIUS,"^2)","=", FUNCTION_4(RADIUS, HEIGHT)," | πr[r+sqr(h^2+r^2)")
            
    elif EQUATIONSELECT== "5": #(4/3)πr^3
        RADIUS = int(input("What is the Radius? " ))
        if VIEWSELECTION == 'd':
            print("(4/3)π",RADIUS,"^3","=", FUNCTION_5(RADIUS))
        if VIEWSELECTION == 'v':
            print("(4/3)π",RADIUS,"^3","=", FUNCTION_5(RADIUS)," | (4/3)πr^3")
    elif EQUATIONSELECT== "6":
        RADIUS = int(input("What is the Radius? " ))
        if VIEWSELECTION == 'd':
            print("4π",RADIUS,"^2","=", FUNCTION_6(RADIUS))
        if VIEWSELECTION == 'v':
            print("4π",RADIUS,"^2","=", FUNCTION_6(RADIUS)," | 4πr^2")
            
    elif EQUATIONSELECT == "q": # Checks for quit again
        print("Thank you!")
        sleep(0.5)
        print("Goodbye!")
        sleep(1)
        exit()
