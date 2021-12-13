#################################################################
# FILE : temperature.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: File that checks if the temperature has risen twice above the threshold temperature.
#################################################################

# descraption: A function that checks if the temperature has risen twice above the threshold temperature.
def is_it_summer_yet(temp0, temp1, temp2, temp3):
    a = [temp1, temp2, temp3]
    i = 0
    for j in a:
        if j>temp0:
            i+=1
    if i>=2:
        return True
    return False


