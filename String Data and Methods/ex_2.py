#Create a variable my_str that stores We are learning Python and it's fun! and
#Find and display the first character.
my_str= "We are learning Python and it's fun!"
first_char = my_str[0]
print(first_char)

#Find and display the character at index 8.
char_index= my_str[8]
print(char_index)

#Find and display the last character (using negative indexing).
last_char = my_str[-1]
print(last_char)

#Find word Python using slicing and display it.
word_python = my_str[16:22]
print(word_python)


#Find word fun using negative slicing and display it.
word_fun = my_str[-4:-1]
print(word_fun)

#Find text lrn (i.e. only some part of text learning) and display it.
part_lrn = my_str[7:12:3]
print(part_lrn)


#Reverse the string and display it.
reversed_str = my_str[::-1]
print(reversed_str)

#Find sub-string that lies from 5th index till end and display it.
from_5_end = my_str[5:]
print(from_5_end)

#Find sub-string that lies from start till 10th index and display it.
start_to_10 = my_str[0:11]
print(start_to_10)