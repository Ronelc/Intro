#################################################################
# FILE : hello_turtle.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that draw a 3 flowers.
#################################################################

import turtle

#description: The function draws a single peta

def draw_petal():
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)

# description: The function draws a single flower

def draw_flower():
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)

# description: The function Draws a single flower
# but also moves the head of the turtle

def draw_flower_and_advance():
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()

# description: The function draws a Three flowers

def draw_flower_bed():
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()

if __name__ == '__main__':
    draw_flower_bed()
    turtle.done()





