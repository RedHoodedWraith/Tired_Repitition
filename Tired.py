"""
I AM TIRED

Date: 13 March 2020
By Rowan Rathod

This is a short and easy script that just creates or overwrites a file called 'tired.txt'
and repeatedly writes the sentence "i am tired".

At each sentence, one letter is capitalised. On the next sentence, the next character is capitalised instead.
This repeats until the end of the sentence is reached, where the capital letter index is return back to the start.
The whole process is repeated  100 times.

Example:
    iteration 1: I am tired
    iteration 2: i Am tired
    iteration 3: i aM tired
    ...
    iteration 8: i am tireD
    iteration 9: I am tired
    iteration 10: i Am tired
"""

file = open("tired.txt", "w+")

sentence = "i am tired"

repeat = 100
index = 0
char_index = 0

while repeat > 0:
    sen_list = list(sentence)

    for i,c in enumerate(sen_list):
        if i == char_index:
            sen_list[i] = c.upper()
    new_sentence = "".join(sen_list)
    new_sentence += "\n"

    file.write(new_sentence)

    char_index += 1
    if char_index >= len(sen_list):
        char_index = 0
    if sen_list[char_index] == " ":
        char_index += 1

    repeat -= 1

file.close()