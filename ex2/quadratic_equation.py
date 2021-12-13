#################################################################
# FILE : quadratic_equation.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: File that solves the Trinom equation.
#################################################################

# descraption: A function that solves the Trinom equation.
def quadratic_equation(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        plus = (-b + d**0.5)/(2*a)
        minus = (-b - d**0.5)/(2*a)
        if plus != minus:
            return plus, minus
        else:
            return plus, None
    else:
        return None, None

# descraption: A function that solves the Trinom equation and also returns the number of solutions.
def quadratic_equation_user_input():
    nums = input("Insert coefficients a, b, and c: ")
    nums1 = nums.split(" ")
    a = nums1[0]
    b = nums1[1]
    c = nums1[2]
    if (float)(a) == 0:
        print("The parameter 'a' may not equal 0")
    else:
        sol1,sol2 = quadratic_equation((float)(a),(float)(b),(float)(c))
        if (sol1 == sol2):
            print("The equation has no solutions")
        elif sol2 == None:
            print("The equation has 1 solution:", sol1)
        else:
            print("The equation has 2 solutions:", sol1,  "and", sol2)



