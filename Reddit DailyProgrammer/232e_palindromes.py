# Written for Python 3.4
# 
# /r/dailyprogrammer Challenge #232 Easy - Palindromes
# https://www.reddit.com/r/dailyprogrammer/comments/3kx6oh/20150914_challenge_232_easy_palindromes/

import sys
import re

def readInput(source):
    with open(source, 'r') as f:
        lines = int(f.readline())
        text = ""
        for i in range(lines):
            text += f.readline()
    return text

def cleanInput(text):
    return re.sub("[^a-z]", "", text.lower())

def checkPalindrome(text):
    isPal = True
    for i,j in zip(text, text[::-1]):
        if i != j:
            isPal = False
            break
    if isPal:
        print("Palindrome")
    else:
        print("Not a palindrome")

if __name__ == "__main__":
    source = sys.argv[1]
    text = readInput(source)
    text = cleanInput(text)
    checkPalindrome(text)