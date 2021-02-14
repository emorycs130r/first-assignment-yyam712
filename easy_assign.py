
'''

This file contains the functions that you need for completing this assignment. 

1. append_two_strings() --> Function to append a string2 to string1. -- 30%
2. append_character() --> Function to append a character to the end of string. -- 30% 
3. append_num_to_string() --> Function to append a number to the end of a string. -- 40%

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''

def append_two_strings(string_1, string_2):
    string_3 = string_1 +" "+ string_2
    return string_3


def append_character(string_1, char_1):
    result = string_1 + char_1
    return result


def append_num_to_string(string_1, num_1):
    answer = string_1 + " " + str(num_1)
    return answer


if __name__ == "__main__":
    
    pass
