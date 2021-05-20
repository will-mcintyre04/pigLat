#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 18:40:13 2021

@author: williammcintyre
"""

# English to Pig Latin
# Will McIntyre
# May 20th, 2021

print('Enter the English message to translate into Pig Latin: ')
message = input()

vowels = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # Blank list of the words in Pig Latin
for word in message.split():
    # Seperate non-letters at start of word
    preNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        preNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(preNonLetters)
        continue