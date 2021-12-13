################################################################
# FILE :wordsearch.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex5 2020
# DESCRIPTION: wordsearch game
#################################################################
import os.path
import sys

MESSEGES = ['The number of parameters is incorrect', 'The word file does not'
            ' exist', 'The matrix file does not exist', 'directions input'
                                                     ' is invalid']
DIRACTIONS_LIST = ['u', 'd', 'r', 'l', 'w', 'x', 'y', 'z']

"""
A function that check if the input is correct and exist,
and returns an appropriate message.
"""
def check_input_args(args):
    msg = None
    if len(args) != 4:
        msg = MESSEGES[0]
    elif not os.path.isfile(args[0]) == True:
        msg = MESSEGES[1]
    elif not os.path.isfile(args[1]) == True:
        msg = MESSEGES[2]
    else:
        for direction in args[3]:
            if direction not in 'udrlwxyz':
                msg = MESSEGES[3]
                break
    return msg

"""
A function that receives a word file, and returns a list of the words in it.
"""
def read_wordlist_file(filename):
    with open(filename) as word:
        line = word.read().splitlines()
        return line

"""
A function that returns the number of rows and columns in the matrix.
"""
def rows_and_cols(filename):
    with open(filename) as matrix:
        lines = matrix.read()
        if lines != '':
            rows = lines.count('\n')
            comma = lines.count(',')
            if rows != 0:
                cols = (comma // rows)+1
            else:
                cols = comma + 1
                rows = 0
        else:
            rows = 0
            cols = 0
        return rows, cols

"""
A function that receives a matrix file,
and returns a 2D list of the matrix letters.
"""
def read_matrix_file(filename):
    list_of_lists = []
    lst = []
    a = rows_and_cols(filename)[0]
    b = rows_and_cols(filename)[1]
    index1 = 0
    index2 = b
    with open(filename) as mat:
        lines = mat.read()
        lines = list(lines)
        for i in lines:
            if ord(i) != 44 and i != '\n':
                lst.append(i)
    while len(list_of_lists) < a:
            list_of_lists.append(lst[index1:index2])
            index1 = index2
            index2 = index1 + b
    return list_of_lists

"""
A function that receives a word and matrix,
and returns the index of the first letter in the word (row,column).
"""
def index_search(word, matrix):
    a = word[0]
    lst = []
    for list in range(len(matrix)):
        for i in range(len(matrix[list])):
            if a == matrix[list][i]:
                lst.append((list, i))
    return lst

"""
A function that makes sure that each search direction appears only once.
"""
def directions(direct):
    str = ''
    for d in direct:
        if d not in str:
            str += d
    return str

"""
A function that gets a matrix word list and directions, and returns a tuple 
with the word and the number of times the word is in the matrix.
"""
def find_words_in_matrix(word_list, matrix, direction):
    if matrix != []:
        lst = []
        mtrx_size = (len(matrix), len(matrix[0]))
        for word in word_list:
            count = 0
            indexes = index_search(word, matrix)
            for indx in indexes:
                row = indx[0]
                col = indx[1]
                for direct in directions(direction):
                    str = ''
                    i = 0
                    while len(str) < len(word) and str != word:
                        if direct == DIRACTIONS_LIST[0]:
                            if row+1 < len(word):
                                break
                            else:
                                str += (matrix[row-i][col])
                                i += 1
                        elif direct == DIRACTIONS_LIST[1]:
                            if mtrx_size[0]-row < len(word):
                                break
                            else:
                                str += (matrix[row+i][col])
                                i += 1
                        elif direct == DIRACTIONS_LIST[2]:
                            if mtrx_size[1]-col < len(word):
                                break
                            else:
                                str += (matrix[row][col+i])
                                i += 1
                        elif direct == DIRACTIONS_LIST[3]:
                            if col+1 < len(word):
                                break
                            else:
                                str += (matrix[row][col-i])
                                i += 1
                        elif direct == DIRACTIONS_LIST[4]:
                            if row+1<len(word) or mtrx_size[1]-col<len(word):
                                break
                            else:
                                str += (matrix[row-i][col+i])
                                i += 1
                        elif direct == DIRACTIONS_LIST[5]:
                            if row+1 < len(word) or col+1 < len(word):
                                break
                            else:
                                str += (matrix[row-i][col-i])
                                i += 1
                        elif direct == DIRACTIONS_LIST[6]:
                            if mtrx_size[0]-row < len(word) or \
                                    mtrx_size[1]-col < len(word):
                                break
                            else:
                                str += (matrix[row+i][col+i])
                                i += 1
                        elif direct == DIRACTIONS_LIST[7]:
                            if mtrx_size[0]-row<len(word) or col+1<len(word):
                                break
                            else:
                                str += (matrix[row+i][col-i])
                                i += 1
                    if str == word:
                        count += 1
            if count != 0:
                lst.append((word, count))
        return lst

"""
A function that receives a list and an output file name.
Returns a file with the results from of the previous function:
find_words_in_matrix.
"""
def write_output_file(results,output_filename):
    with open(output_filename, 'w') as output_file:
        if results == []:
            file = output_filename
        else:
            for result in results:
                pair = result[0]+','+str(result[1])
                output_file.writelines(pair)
                if results.index(result) != len(results)-1:
                    output_file.write('\n')

"""
The main function that calls all functions, and runs the game.
"""
def main():
    arg = sys.argv[1::]
    if check_input_args(arg) == None:
        word_lst = read_wordlist_file(arg[0])
        matrix_lst = read_matrix_file(arg[1])
        direct = arg[3]
        return_lst = find_words_in_matrix(word_lst, matrix_lst, direct)
        write_output_file(return_lst, arg[2])
    else:
        print(check_input_args(arg))

if __name__ == '__main__':
    main()

