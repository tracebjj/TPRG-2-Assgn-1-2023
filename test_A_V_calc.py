'''
TPRG 2131 Fall 2023 Assignment 1
Sept, 2023
Phil J <philip.jarvis@durhamcollege>


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.

TPRG 2131 Fall 2023 Assignment 1
October, 2023
Trace C <trace.carter@dcmail.ca>
'''

from A_V_calc.py import FUNCTION_1

def test_FUNCTION_1(): #Width, Height, Length = V
    assert FUNCTION_1(12, 4, 16) == 768
    assert FUNCTION_1(2, 6, 5) == 60
    assert FUCNTION_1(2.7,9,17) == 413.1
def test_FUNCTION_2(): #W, H, L
    assert FUNCTION_2(1,5,34) == 418
    assert FUNCTION_2(7,19,43) == 2502
    assert FUNCTION_2(0.5,90,56) == 10226
    
def test_FUNCTION_3(): # Cone Volume
    assert FUNCTION_3(7,9) == 461.81
    assert FUNCTION_3(8,1) == 67.02
    assert FUNCTION_3(13,4.5) == 796.39
def test_FUNCTION_4(): # Cone Area
    assert FUNCTION_4(4,6) == 140.88
    assert FUNCTION_4(6,4) == 249.02
    assert FUNCTION_4(10,9) == 736.82
    
def test_FUNCTION_5(): # Sphere Volume
    assert FUNCTION_5(5) == 523.6
    assert FUNCTION_5(9) == 3053.63
    assert FUNCTION_5(3) == 113.1
def test_FUNCTION_6(): # Area
    assert FUNCTION_6(2) == 50.27
    assert FUNCTION_6(4) == 201.06
    assert FUNCTION_6(7) == 615.75
    
    