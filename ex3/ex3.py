#################################################################
# FILE : ex3.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex3 2020
# DESCRIPTION: Loops exercise.
#################################################################

"""
A function that receives a list of numbers, and returns them
plus their sum.
"""
def input_list():
    my_input = input()
    sum = 0
    lst = []
    if my_input == "":
        return [0]
    else:
        while my_input != "":
            lst.append(float(my_input))
            sum += float(my_input)
            my_input = input()
        lst.append(sum)
    return lst

"""
A function that accepts two lists of numbers - vectors,
multiply them by one another and sum them up.
"""
def inner_product(vec_1, vec_2):
    lst = []
    sum = 0
    if len(vec_1) == 0 and len(vec_2) == 0:
        return (0)
    if len(list(vec_1)) != len(list(vec_2)):
        return None
    else:
        for i in range(len(vec_1)):
            sum += (vec_1[i] * vec_2[i])
    return sum

# descraption: The following code snippet checks a series monotony by several
# functions.
"""
A function that checks whether the sequence is monotonically increasing.
"""
def inc(seq):
    a = seq[0]
    for i in seq[1:]:
        if i >= a:
            a = i
        else:
            return False
    return True

""""
A function that checks whether the sequence is strictly increasing.
"""
def str_inc(seq):
    a = seq[0]
    for i in seq[1:]:
        if i > a:
            a = i
        else:
            return False
    return True

"""
A function that checks whether the sequence is monotonically decreasing.
"""
def dec(seq):
    a = seq[0]
    for i in seq[1:]:
        if i <= a:
            a = i
        else:
            return False
    return True

"""
A function that checks whether the sequence is strictly decreasing.
"""
def str_dec(seq):
    a = seq[0]
    for i in seq[1:]:
        if i < a:
            a = i
        else:
            return False
    return True

"""
A function that checks whether the sequence is decreasing, strictly or 
strictly strictly/decreasing.
"""
def sequence_monotonicity(sequence):
    if len(sequence) < 2:
        return [True, True, True, True]
    else:
        seq = sequence
        lst = [inc(seq), str_inc(seq), dec(seq), str_dec(seq)]
        return(lst)

"""
A function that accepts a list of 4 boolean elements (True or False),and 
returns a list of 4 numbers Representing a final series which is basically 
an example of a series that holds the settings depending on where True is 
in the input
"""
def monotonicity_inverse(def_bool):
    a = def_bool
    if bool(a[0])+bool(a[1])+bool(a[2])+bool(a[3])>bool(1)+bool(1)\
    or a[1]==True and a[2]==True or a[0]==True and a[3]==True:
        return None
    elif a[0] == True:
        if a[1] == True:
            return [1, 2, 3, 4]
        elif a[1] == False:
            if a[2]==True:
                return  [1, 1, 1, 1]
            else:
                return [1,2,2,3]
    elif a[2] == True:
        if a[3] == True:
            return [4,3,2,1]
        else:
            return [4,4,3,3]
    elif a[0]==a[1]==a[2]==a[3]:
        return [1, 0, -1, 1]
    else:
        return None


# discraption: A code snippet that returns the "n" primes numbers.
"""
A function that returns True if the number is prime.
"""
def primes(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

"""
A function that returns the "n" primes numbers.
"""
def primes_for_asafi(n):
    lst =[]
    num = 2
    while len(lst) < n:
        if primes(num):
            lst.append(num)
        num += 1
    return lst

"""
A function that gets a list of vectors and connects them to a coordinate 
coordinate.
"""
def sum_of_vectors(vec_lst):
    new_vec = []
    if len(vec_lst)==0:
        return None
    for vec in vec_lst:
        if len(vec) == 0:
            return []
    for j in range(len(vec)):
        sum = 0
        for k in range(len(vec_lst)):
            sum+=vec_lst[k][j]
        new_vec.append(sum)
    return new_vec

"""
Receipt function List of vectors (list of lists) and returns the pair number 
of the lists that orthogonal to each other.
"""
def num_of_orthogonal(vectors):
    lst =[]
    for i in range(len(vectors)):
        for j in range(i+1,len(vectors)):
            lst.append(inner_product(vectors[i],vectors[j]))
    return lst.count(0)

