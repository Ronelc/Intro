#################################################################
# FILE : shapes.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A file that calculates space shapes.
#################################################################
import math

# descraption: A function that calculates a circle area.
def circle():
    r = (float)(input())
    return math.pi * r ** 2

# descraption: A function that calculates a rectangle area.
def rect():
    row = (float)(input())
    col = (float)(input())
    return row * col

# descraption: A function that calculates an equilateral triangle area.
def tria():
    a = (float)(input())
    return ((3 ** 0.5) / 4) * a ** 2

# descraption: A function that calculates space shapes.
def shape_area():
    shape = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if shape == '1':
        return circle()
    elif shape == '2':
       return rect()
    elif shape == '3':
        return tria()
    else :
        return None


