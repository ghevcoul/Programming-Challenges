# Written for Python 3.4
# 
# /r/dailyprogrammer Challenge #238 Easy - Consonants and Vowels
# https://www.reddit.com/r/dailyprogrammer/comments/3q9vpn/20151026_challenge_238_easy_consonants_and_vowels/

import sys
import random

letters = {
    'v':"aeiou",
    'V':"AEIOU",
    'c':"bcdfghjklmnpqrstvwxyz",
    'C':"BCDFGHJKLMNPQRSTVWXYZ"
}

template = sys.argv[1]

word = []
for i in template:
    try:
        word.append(random.choice(letters[i]))
    except KeyError:
        sys.exit("Invalid input!")
print(''.join(word))

