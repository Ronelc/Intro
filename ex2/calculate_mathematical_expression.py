#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A file that accepts two numbers and an account operation, and returns a resul.
#################################################################

# descraption: A function that calculates account operations.
def calculate_mathematical_expression(num1, num2, math):
    if math == '+':
        return num1+num2
    elif math == '-':
        return num1-num2
    elif  math == '*':
        return num1 * num2
    elif math == '/' and num2 != 0:
        return num1 / num2
    return

# descraption: A function that calculates account operations, In conversion from string.
def calculate_from_string(str):
    a = str.split(" ")
    b = calculate_mathematical_expression((float)(a[0]), (float)(a[2]), a[1])
    return b




   
