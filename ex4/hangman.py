################################################################
# FILE :hangman.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex4 2020
# DESCRIPTION: hangman game
#################################################################
import hangman_helper

MESSASAGES = ['Input is invalid.','The letter was previously selected.',
              'Wrong guess, please try again.','Correct guess, well done!',
              '','You won Well done!!',
              'you lose, The word is: {}', 'The number of games you have '
              'played is: {}. The points you gained is: {}.'  
              'Do you want to play again?','The number of games you have '
              'played is: {}. Do you want to play again?','Lets get started']

"""
A function that puts a letter in the appropriate place in the pattern.
"""
def update_word_pattern(word, pattern, letter):
    indx = 0
    string = ''
    lst_pattern = list(pattern)
    for let in word:
        indx += 1
        if let == letter:
         lst_pattern[indx-1:indx] = [letter]
    for j in lst_pattern:
     string += j
    return string

"""
A function that checks how many times the letter is in the word.
"""
def counter(pattern,user_input):
    count = 0
    new_count = 0
    for i in pattern:
        for j in user_input:
            if i == j:
                count+=1
        new_count += len(user_input)-count
    return int((new_count)**0.5)

"""
A function that matches words to a pattern where the letter is visible.
"""
def right_place(word,pattern,wrong_guess_lst):
    i = 0
    for stp in pattern:
        if stp != '_':
            if word[i] != stp or pattern.count(stp)!= word.count(stp):
                return False
        i+=1
    for let in word:
        if let in wrong_guess_lst:
            return False
    return True

"""
A function that returns a list of similar words to the 
requested word is used to hint.
"""
def filter_words_list(words, pattern, wrong_guess_lst):
    gusess_lst = []
    for word in words:
        if len(word) == len(pattern) and\
                right_place(word,pattern,wrong_guess_lst):
            gusess_lst.append(word)
    return gusess_lst

"""
A function that returns us the final clue list.
"""
def finle(lst):
    finle_lst = []
    i=0
    m = hangman_helper.HINT_LENGTH
    if len(lst) <= m:
        finle_lst = lst
    else:
        while len(finle_lst) < m:
            finle_lst.append(lst[(i*len(lst))//m])
            i+=1
    return finle_lst

"""
A function that gets a word list, and a number of points with which 
the player starts the game and runs a single game.
"""
def run_single_game(words_list, score):
    previous_selections_lst = []
    wrong_guess_lst = []
    word = hangman_helper.get_random_word(words_list)
    pattern = len(word)*'_'
    hangman_helper.display_state(pattern, wrong_guess_lst, score,
                                 MESSASAGES[9])
    while score > 0 and pattern != word:
        user_input = hangman_helper.get_input()
        if user_input[0] == hangman_helper.LETTER:
            user_input = user_input[1]
            if len(user_input)!=1 or ord(user_input)<97 or 122<ord(user_input):
                msg = MESSASAGES[0]
                hangman_helper.display_state\
                    (pattern, wrong_guess_lst, score, msg)
            else:
                flag = False
                for i in previous_selections_lst:
                    if user_input == i:
                        msg = MESSASAGES[1]
                        hangman_helper.display_state(pattern, wrong_guess_lst,
                                                     score, msg)
                        flag = True
                        break
                if flag:
                    continue
                previous_selections_lst.append(user_input)
                count = 0
                score -= 1
                for lett in word:
                    if user_input == lett:
                        count+=1
                if count == 0:
                    wrong_guess_lst.append(user_input)
                    if score != 0:
                        msg = MESSASAGES[2]
                        hangman_helper.display_state(pattern, wrong_guess_lst,
                                                     score, msg)
                else:
                    msg = MESSASAGES[3]
                    pattern = update_word_pattern(word, pattern,
                                                  user_input)
                    score += ((count * (count + 1)) // 2)
                    if pattern != word:
                        hangman_helper.display_state(pattern,
                                            wrong_guess_lst, score, msg)
                previous_selections_lst.append(user_input)
        elif user_input[0] == hangman_helper.WORD:
            user_input = user_input[1]
            score-=1
            if user_input == word:
                new_count = counter(pattern,user_input)
                pattern = word
                score += ((new_count * (new_count + 1)) // 2)
            else:
                if score!= 0:
                    msg = MESSASAGES[2]
                    hangman_helper.display_state(pattern, wrong_guess_lst,
                                         score, msg)
        elif user_input[0] == hangman_helper.HINT:
            matches = filter_words_list (words_list,
                                         pattern, wrong_guess_lst)
            matches = finle(matches)
            score -= 1
            msg = MESSASAGES[4]
            hangman_helper.show_suggestions(matches)
            if score != 0:
                hangman_helper.display_state(pattern, wrong_guess_lst,
                                        score, msg)
    if pattern == word:
        msg = MESSASAGES[5]
    else:
        msg = MESSASAGES[6].format(word)
    hangman_helper.display_state(pattern, wrong_guess_lst, score, msg)
    return score

"""
The main function that runs the game.
"""
def main():
    num_of_games = 0
    word_list = hangman_helper.load_words()
    score = run_single_game(word_list,hangman_helper.POINTS_INITIAL)
    while score>=0:
        num_of_games += 1
        if score == 0:
            msg = MESSASAGES[8].format(num_of_games)
            if hangman_helper.play_again(msg) == True:
                num_of_games = 0
                run_single_game(word_list,hangman_helper.POINTS_INITIAL)
            else:
                break
        else:
            msg = MESSASAGES[7].format(num_of_games, score)
            if hangman_helper.play_again(msg) == True:
                score = run_single_game(word_list, score)
            else:
                break

if __name__ == '__main__':
    main()












