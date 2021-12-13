#################################################################
# FILE : largest_and_smallest.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A file that finds the maximum and minimum number.
# I chose the last two inputs because one has a negative value and the other has similar values ​​in all variables
#################################################################

# descraption: A function that finds the maximum and minimum number.
def largest_and_smallest(num1, num2, num3):
    max_val = num1
    min_val  = num2
    a = [num1,num2,num3]
    for i in a:
        if i>max_val:
            max_val = i
        elif i< min_val:
            min_val = i
    return max_val, min_val

# descraption: Test function.
def check_largest_and_smallest():
    i = 0
    if largest_and_smallest(17, 1, 6) == (17, 1):
        i+=1
    if largest_and_smallest(1, 17, 6) == (17, 1):
        i+=1
    if largest_and_smallest(1, 1, 2) == (2, 1):
        i += 1
    if largest_and_smallest(8, 8, 8) == (8, 8):
        i += 1
    if  largest_and_smallest(0, -1, 9) == (9, -1):
        i += 1
    if i==5:
        return True
    return False



