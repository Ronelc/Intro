################################################################
# FILE :ex7.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex7 2020
# DESCRIPTION: Recursion Exercise
#################################################################

"""
A function that receives a number and prints the integers
from 1 to the number includes, in ascending order with 'None' at the end.
"""
def help_print(n):
    if n < 1:
        return
    else:
        help_print(n - 1)
        print(n)

"""
A function that receives a number and prints the integers
from 1 to the number includes, in ascending order.
"""
def print_to_n(n):
    if help_print(n) == n:
        return

"""
Auxiliary function that receives a number and a list and returns
the sum of the number.
"""
def help_sum(n, lst):
    if n != 0:
        k = str(n)
        if len(k) == 0:
            return
        if len(k) == 1:
            lst.append(int(k))
        else:
            num = int(n/(int('1'+'0'*(len(k)-1))))
            lst.append(num)
            k = list(k)
            i = k.index(str(num))
            del(k[i])
            k = ''.join(k)
            help_sum(int(k), lst)
        return lst
    return []

"""
A function that accepts a number and returns the sum of the number.
"""
def digit_sum(n):
    if n < 0:
        return
    else:
        return (sum(help_sum(n, [])))

"""
A function that accepts two numbers: n, i and checks whether n have a
divisor is smaller than i.
"""
def has_divisor_smaller_than(n, i):
    if i == 1:
        return True
    else:
        if n % i != 0:
            return has_divisor_smaller_than(n, i - 1)

"""
A function that receives a number and checks if it is a prime number.
"""
def is_prime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    else:
        result = has_divisor_smaller_than(n, int(n**(1/2)))
        if result == True:
            return True
        else:
            return False

"""
A function that solves the "Hanoi towers" game.
"""
def play_hanoi(hanoi, n, src, dst, temp):
    if n <= 0:
        return
    if n == 1:
        hanoi.move(src, dst)
    else:
        play_hanoi(hanoi, n - 1, src, temp, dst)
        hanoi.move(src, dst)
        play_hanoi(hanoi, n - 1, temp, dst,  src)

"""
list of characters and number. And returns all possible combinations of 
the number length when each character can appear more than once.
"""
def help_sequences(char_lst, n, sub):
    if len(sub) == n:
        print(sub)
    else:
        for i in char_lst:
            help_sequences(char_lst, n, sub+i)

"""
A function that accepts list and number and returns all possible combinations 
of the number length when each character can appear more than once.
"""
def print_sequences(char_list, n):
    if n == 0 or char_list == []:
        print('')
    else:
        help_sequences(char_list, n, '')

"""
list of characters and number. And returns all possible combinations of 
the number length when each character can appear only once.
"""
def help_repetition(char_lst, n, sub):
    if len(sub) == n:
        print(sub)
    else:
        for i in char_lst:
            if i not in sub:
                help_repetition(char_lst, n, sub+i)

"""
A function that accepts list and number and returns all possible combinations 
of the number length when each character can appear only once.
"""
def print_no_repetition_sequences(char_list, n):
    if n == 0 or char_list == []:
        print('')
    else:
        help_repetition(char_list, n, '')

"""
Function that accepts: Integer List: n, empty String , and empty List and
returns a list of possible strings of n length.
"""
def help_parentheses(lst, n, result, new):
    if len(result) == n:
        if result[0] != ')' and result[-1] != '(' and result[0:n//2].count('(')\
    >= result[n//2:-1].count('(') and result.count('(') == result.count(')'):
            new.append(result)
    else:
        for i in lst:
            help_parentheses(lst, n, result+i, new)
    return new

"""
A function that receives an integer: n and returns a list of all valid
strings of n length.
"""
def parentheses(n):
    if n <= 0:
        return ['']
    else:
        lst = help_parentheses(['(', ')'], 2*n, '', [])
        lst1 = lst[:]
        for arg in lst:
            k = 0
            for sign in arg:
                if sign == '(':
                    k += 1
                elif sign == ')':
                    k -= 1
                    if k < 0:
                        lst1.remove(arg)
                        break
    return lst1

"""
The function that gets a 2D array consisting of the characters: "." And "*" 
and start point. And replaces the characters "." Characters "*" start from the 
starting point  according to the rules.
"""
def flood_fill(image, start):
    a, b = start[0], start[1]
    if image[a][b] == '*':
        return
    else:
        image[a][b:b+1] = '*'
        flood_fill(image, (start[0]-1, start[1]))
        flood_fill(image, (start[0]+1, start[1]))
        flood_fill(image, (start[0], start[1]-1))
        flood_fill(image, (start[0], start[1]+1))
