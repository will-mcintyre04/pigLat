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
    while len(word) > 0 and not word[0].isalpha(): # While the start of the word is not an alpha (a letter), add to prenonletters
        preNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(preNonLetters) 
        continue
    
    # Seperate the non letters at the end of the word
    endNonLetters = ''
    while not word[-1].isalpha():
        endNonLetters += word[-1]
        word = word[:-1]
    
    # Remember if word was upper or title
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    
    word = word.lower() # make the word lowercase for translation
    
    # Seperate the consonants at the start of word
    preConsonants = ''
    while len(word) > 0 and not word[0] in vowels:
        preConsonants += word[0]
        word = word[1:]
        
    # Add pig latin ending to the word
    if preConsonants != '':
        word += preConsonants + 'ay'
    else:
        word += 'yay'
        
    # Set word back to upper or title:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    # Add non letters back to the start or end of word
    pigLatin.append(preNonLetters + word + endNonLetters)

# Join all back into a single string
print(' '.join(pigLatin))
    