# Written for Python 3.4
# 
# /r/dailyprogrammer Challenge #192 Intermediate - Markov Chain Error Detection
# https://www.reddit.com/r/dailyprogrammer/comments/2ovt2i/20141210_challenge_192_intermediate_markov_chain/


import sys
import os.path
from string import ascii_lowercase as letters

##############################
# Reads a wordlist from a file and generates
# a matrix of the frequency of letter pairs
# such that matrix[first][second] is the occurence
# of first-second
def generateMarkov(source):
  # Check if we already have the Markov chain data cached
  if os.path.exists("markov.dat"):
    # Check if it was written with the same wordlist
    #print("Found cached chain data.")
    reader = open("markov.dat", 'r')
    wordfile = reader.readline().strip()
    if wordfile == source:
      #print("Using same wordlist.")
      # Read in existing data
      markov = reader.readlines()
      matrix = []
      for line in markov:
        elems = line.split()
        temp = []
        for i in elems:
          temp.append(float(i))
        matrix.append(temp)
    else:
      #print("Using different wordlist.")
      matrix = calcChainData(source)
    reader.close()
  else:
    #print("No cached chain data detected.")
    matrix = calcChainData(source)
  
  return matrix  

def calcChainData(source):
  # Read in wordlist
  reader = open(source, 'r')
  words = reader.readlines()
  reader.close()
  
  # Initialize matrix
  matrix = [x[:] for x in [[0]*26]*26]
  
  # Make the frequency matrix
  for w in words:
    word = w.strip().lower()
    for i in range(len(word)-1):
      matrix[lett[word[i]]][lett[word[i+1]]] += 1
  
  # Convert count to percent occurence
  numWords = len(words)
  for i in range(26):
    for j in range(26):
      matrix[i][j] = matrix[i][j] / numWords
  
  # Write matrix to file for caching
  writer = open("markov.dat", 'w')
  writer.write(source+"\n")
  for i in matrix:
    for j in i:
      writer.write("{0:> 8.5f}".format(j))
    writer.write("\n")
  writer.close()
  
  return matrix

##############################
# Takes a word to test and checks each letter pair
# to see if its occurence in the Markov chain data
# is below a cutoff.
def testWord(word):
  cutoff = 0.0001
  print('For the word: "{0}"...'.format(word))
  for i in range(len(word)-1):
    print("The letter pair {0} occurs in {1:> 8.5f}% of words.".format(word[i:i+2], matrix[lett[word[i]]][lett[word[i+1]]]))
    if matrix[lett[word[i]]][lett[word[i+1]]] < cutoff:
      print("   ...and is unlikely to be correct.")

##############################
test = sys.argv[1]
wordlist = "corncob_lowercase.txt"

# Lazily create a dictionary with the position 
# of each letter in the alphabet
lett = {}
for i, a in enumerate(letters):
  lett[a] = i

matrix = generateMarkov(wordlist)

testWord(test)

