# -*- coding: utf-8 -*-

"""
Created on Thu Feb 18 11:21:52 2021

@author: w7k-j
@https://github.com/W7k-J
"""

import random

def char_changer(word, word_hidden, char):
    temp_list = list(word_hidden) 
    for idk, k in enumerate(word):
        if k == char:
            temp_list[idk] = char
    return "".join(temp_list)

def game():    
    dictionary = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(dictionary)
    word_hidden = "-" * len(word)
    total = 0
    letter_tried = []
    
    while True:
        print(word_hidden)
        char = input("Input a letter: ")
        if len(char) != 1:
            print("You should input a single letter")
            print("")
            continue
        if not char.islower():
            print("Please enter a lowercase English letter")
            print("")
            continue
        if char in letter_tried:
            print("You've already guessed this letter")
            print("")
            continue
        
    
        letter_tried.append(char)
        
        if char in word:
            word_hidden = char_changer(word, word_hidden, char)
        else:
            total += 1
            print("That letter doesn't appear in the word")
        
    
        if word_hidden == word:
            print("You guessed the word {word}!")
            print("You survived!")
            break
        if total == 8:
            print("You lost!")
            break
        print("")
        
    
    
print("H A N G M A N")
while True:
    pytanie = input('Type "play" to play the game, "exit" to quit: ')
    if pytanie == "play":
        print("")
        game()
    else:
        break


