#################################################################
# FILE : math_print.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that print a math functions.
#################################################################

import math

# DESCRIPTION: The function prints the golden ratio

def golden_ratio():
 print((1+5**(1/2))/2)

# DESCRIPTION: The function prints the value of 6^2

def six_squared():
 print(6**2)

# DESCRIPTION: The function prints the excess length in a
# right-angled triangle whose ribs 12 and 5 in length

def hypotenuse():
 print((5**2+12**2)**(1/2))

# DESCRIPTION: The function prints the value of the number pi
def pi():
 print(math.pi)

# DESCRIPTION: The function prints the value of the number e

def e():
 print(math.e)

# DESCRIPTION: A function that prints squares, with rib lengths from 1 to 10

def squares_area():
 print(1**2, 2**2, 3**2, 4**2, 5**2, 6**2, 7**2, 8**2, 9**2, 10**2)

if __name__ == '__main__':
 golden_ratio()
 six_squared()
 hypotenuse()
 e()
 pi()
 squares_area()



