################################################################
# FILE :hangman.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex4 2020
# DESCRIPTION:
#################################################################
import hangman_helper

"""

"""
def update_word_pattern(word, pattern, letter):
    count = 0
    string = ''
    lst_pattern = list(pattern)
    for let in word:
        count += 1
        if let == letter:
         lst_pattern.insert(count-1 ,letter)
         lst_pattern.pop(count)
    for j in lst_pattern:
     string += j
    return string
print(update_word_pattern('hii', '___', 'h'))
"""
a function that return a random word.
"""
def a_word():
    return (hangman_helper.get_random_word(hangman_helper.load_words()))

def init_game():
    wrong_gusses_lst = 0
    a_word()
    pattern = len(a_word())*'_'

def user_input():
    a = hangman_helper.get_input()
    if len(a) > 1 or a != a.lower():
        msg = 'Input is incorrect'
    elif :
        msg = 'The letter was previously selected'
    elif len(a) == 1:
        score -= 1
        update_word_pattern(a_word(), pattern, a)
        for j in a_word():
            count = 0
            if a == j:
            count+=1
            scote += ((count*(count+1))//2)
            else a != j:
            wrong_lst+=1




def prosses_game():
    while count > 0 or pattern != a_word():
        init_game()
        update_word_pattern(a_word(),pattern, user_input())
        hangman_helper.display_state(pattern, wrong_guess_lst, points, msg)