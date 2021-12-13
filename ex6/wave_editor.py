################################################################
# FILE :wave_editor.py
# EXERCISE : intro2cs2 ex6 2020
# DESCRIPTION: wav audio file editing software.
#################################################################
import wave_helper as help
import math
import os

DICT = {'CHANGE':'1', 'COMPOS':'2', 'EXIT':'3', 'FLIP':'1', 'NEGATIVE':'2',
        'SPEED':'3', 'SLOW':'4', 'UP':'5', 'DOWN':'6', 'FILTER':'7', 'END':'8'}
FREQUE = {'A':440, 'B':494, 'C':523, 'D':587, 'E':659, 'F':698, 'G':784, 'Q':0}
START_MENU = ('To change the wav file, enter: 1.\nTo compose a tune,'
              ' enter: 2.\nTo exit the program enter: 3 \n')
MENU = ('You can make the following changes: \nTo flip file enter: 1.\n' 
       'To negate the audio, enter 2.\nTo speed up, enter: 3.\n'
       'To slow down, enter: 4.\nTo increase volume enter: 5.\n'
       'For decrease the volume, enter: 6.\nFor low pass filter enter: 7.\n'
       'To the end menu, enter: 8 \n')
DONE_MSG = "{} was done successfully"
ERROR_MSG = 'Invalid input '
FILE_EROR = 'File does not exist'
NEGATIVE_FUNC = -1
SPEED_FUNC = 2
MULTI_FUNC = 1.2
DIFF_FUNC = 1.2
SAMPLE_RATE = 2000
SECONDS = 16
MAX_VOLIUM = 32767
MIN_VOLIUM = -32768

"""
This function flips the order of the values, from the beginning to the end.
:param audio_data: the file
:return:the flipped order of the values
"""
def flip(audio_data):
      return audio_data[::-1]

"""
 This ia a help function which arranges a list of numbers to a list of pairs.
:param audio_data: audio file
:param new_lst: the new list
"""
def org(audio_data, new_lst):
      finle_lst = []
      a = 0
      while len(finle_lst) < len(audio_data):
            b = a + 2
            finle_lst.append(new_lst[a:b])
            a += 2
      return finle_lst

"""
this function gives to the values in the list their negative value
:param audio_data: audio file
:return: the negative value of the values in the list
"""
def negate(audio_data):
      new_lst = []
      for lst in audio_data:
            for arg in lst:
                  if arg == MIN_VOLIUM:
                        arg = MAX_VOLIUM
                  else:
                        arg = NEGATIVE_FUNC*arg
                  new_lst.append(arg)
      return org(audio_data, new_lst)

"""
This function speeds the velocity of the melody
:param audio_data: the audio file
:return: the altered melody
"""
def speed(audio_data):
      new_lst = []
      for i in range(len(audio_data)):
            if i % SPEED_FUNC == 0:
                  new_lst.append(audio_data[i])
      return new_lst

"""
This function slows the original piece of music
:param audio_data: the audio file
:return: the altered melody
"""
def slow(audio_data):
      new_lst = []
      a = 0
      if audio_data != []:
            new_lst.append(audio_data[a])
            while len(new_lst) < 2*len(audio_data)-1:
                  b = a + 1
                  left = int((audio_data[a][0]+audio_data[b][0])/2)
                  right = int((audio_data[a][1]+audio_data[b][1])/2)
                  new_lst.append(list((left, right)))
                  new_lst.append(audio_data[b])
                  a += 1
            return new_lst
      return []

"""
This function highs the volume of the melody
:param audio_data: the audio file
:return: a louder melody
"""
def increase(audio_data):
      new_lst = []
      if audio_data != []:
            for lst in audio_data:
                  for arg in lst:
                        arg *= MULTI_FUNC
                        if arg > MAX_VOLIUM:
                              arg = MAX_VOLIUM
                        elif arg < MIN_VOLIUM:
                              arg = MIN_VOLIUM
                        new_lst.append(int(arg))
            return org(audio_data, new_lst)
      return []

"""
This function lowers the volume of the melody
:param audio_data: audio file
:return: a lower melody
"""
def dicrease(audio_data):
      new_lst = []
      if audio_data != []:
            for lst in audio_data:
                  for arg in lst:
                        arg /= DIFF_FUNC
                        new_lst.append(int(arg))
            return org(audio_data, new_lst)
      return []
"""
 This function dims the melody
:param audio_data: the audio file
:return: the dimmed melody
"""
def low_pass_filter(audio_data):
      new_lst = []
      a = 0
      if audio_data != []:
            if len(audio_data) == 1:
                  return audio_data
            else:
                  new_lst.append([int((audio_data[0][0]+audio_data[1][0])/2),
                                  int((audio_data[0][1]+audio_data[1][1])/2)])
                  while len(new_lst) < len(audio_data)-1:
                        b = a + 1
                        c = b + 1
                        left = int((audio_data[a][0]+audio_data[b][0]+
                                    audio_data[c][0])/3)
                        right = int((audio_data[a][1]+audio_data[b][1]+
                                     audio_data[c][1])/3)
                        new_lst.append(list((left, right)))
                        a += 1
                  new_lst.append([int((audio_data[-1][0]+audio_data[-2][0])/2),
                                  int((audio_data[-1][1]+audio_data[-2][1])/2)])
            return new_lst
      return []


"""
this is auxiliary function that receives user input and audio list.
Then, it returns  an updated audio list and appropriate message.
:param s_user_input: a flipped audio file
:param audio_data: the audio file
:return: an updated audio list and a message
"""
def selection(s_user_input, audio_data):
      msg = ''
      if s_user_input == DICT['FLIP']:
            audio_data = flip(audio_data)
            msg = 'flip file'
      elif s_user_input == DICT['NEGATIVE']:
            audio_data = negate(audio_data)
            msg = 'Audio deprivation'
      elif s_user_input == DICT['SPEED']:
            audio_data = speed(audio_data)
            msg = 'Accelerate file'
      elif s_user_input == DICT['SLOW']:
            audio_data = slow(audio_data)
            msg = 'Slowing down the file'
      elif s_user_input == DICT['UP']:
            audio_data = increase(audio_data)
            msg = 'The volume increasing'
      elif s_user_input == DICT['DOWN']:
            audio_data = dicrease(audio_data)
            msg = 'The volume decreasing'
      elif s_user_input == DICT['FILTER']:
            audio_data = low_pass_filter(audio_data)
            msg = 'the low pass filter'
      return (audio_data, msg)

"""
this function reads the wav file
:return: the sample rate, the audio file and the audio
"""
def read():
      file_name = input('Please write the file name you would like to read \n')
      file = help.load_wave(file_name)
      while file == -1:
            print(FILE_EROR)
            file_name = input(
                  'Please write the file name you would like to read \n')
            file = help.load_wave(file_name)
      else:
            sample_rate = file[0]
            audio_data = file[1]
            return sample_rate, audio_data, file_name
      
"""
This function runs the changes in the file
:param sample_rate: the number of sampling
:param audio_data: the audio file
:param file_name: the file's name
:return: the changes in the file
"""
def change_file(sample_rate, audio_data, file_name):
      s_user_input = input(MENU)
      while s_user_input != DICT['END']:
            if s_user_input not in [DICT['FLIP'],DICT['NEGATIVE'],DICT['SPEED']
                  ,DICT['SLOW'], DICT['UP'], DICT['DOWN'], DICT['FILTER']]:
                  print(ERROR_MSG)
                  s_user_input = input(MENU)
            else:
                  result = selection(s_user_input, audio_data)
                  audio_data = result[0]
                  print(DONE_MSG.format(result[1]))
                  s_user_input = input(MENU)
      else:
            file_name = input('Please enter a file name where '
                              'you want to save the changes\n')
            save = help.save_wave(sample_rate, audio_data, file_name)
            while save != 0:
                  print(ERROR_MSG)
                  file_name = input('Please enter a file name where '
                                    'you want to save the changes\n')
            f_user_input = input(START_MENU)
            return f_user_input

"""
This function opens the file of the melody and then the melody
function uses this
:return: the melody file
"""
def open_file():
      file = input('Please enter the file name with'
                         ' the composition guidelines\n')
      finle_lst = []
      while not os.path.exists(file):
            print(FILE_EROR)
            file = input('Please enter the file name with'
                         ' the composition guidelines\n')
      else:
            with open(file) as file:
                  lines = file.read().split()
            lines = list(lines)
            lst = org(lines, lines)
            for i in lst:
                  if i != []:
                        finle_lst.append(i)
            return finle_lst

"""
This function composes the melody
:return: the composed melody
"""
def compos():
      lst = open_file()
      new_lst = []
      if lst != []:
            for tpl in lst:
                  frequency = FREQUE[tpl[0]]
                  sec = int(tpl[1])
                  for i in range(int(sec * SAMPLE_RATE / SECONDS)):
                        samp = MAX_VOLIUM * math.sin(math.pi * 2 *
                                          (i * frequency / SAMPLE_RATE))
                        new_lst.append(list((int(samp), int(samp))))
            return new_lst

"""
This is the function that runs everything
:return: the main function
"""
def start_program():
      f_user_input = input(START_MENU)
      while f_user_input not in [DICT['CHANGE'], DICT['COMPOS'], DICT['EXIT']]:
            print(ERROR_MSG)
            f_user_input = input(START_MENU)
      else:
            audio_data = ''
            while f_user_input != DICT['EXIT']:
                  if f_user_input == DICT['CHANGE']:
                        var = read()
                        f_user_input = change_file(var[0], var[1], var[2])
                  if f_user_input == DICT['COMPOS']:
                        audio_data = compos()
                        file_name = 'temporary'
                        f_user_input = change_file(SAMPLE_RATE, audio_data,
                                                   file_name)
                  if f_user_input == DICT['EXIT']:
                        break

if __name__ == '__main__':
    start_program()