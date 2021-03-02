# -*- coding: utf-8 -*-

"""
Created on Thu Feb 18 11:21:52 2021

@author: w7k-j
@https://github.com/W7k-J
"""


import random


print("H A N G M A N")
dictionary = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(dictionary)

# word_hidden = word[:3] + ("-") * (len(word)-3)

# guess = input(f"Guess the word {word_hidden}: ")

# if guess == word:
#     print("You survived!")
# else:
#     print("You lost!")

# print('The game will be available soon.')

# print(word)

def char_changer(word, word_hidden, char):
    temp_list = list(word_hidden) 
    for idk, k in enumerate(word):
        if k == char:
            temp_list[idk] = char
    return "".join(temp_list)

 


word_hidden = "-" * len(word)
total = 0


while total < 8:
    total += 1
    # print(total)
    char = input("Input a letter:")
    if char not in word:
        print("That letter doesn't appear in the word")
    else:
        word_hidden = char_changer(word, word_hidden, char)
        print(word_hidden)
    
    
print("Thanks for playing\"!")
print("We'll see how well you did in the next stage")