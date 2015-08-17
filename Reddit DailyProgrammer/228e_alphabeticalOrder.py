# Written for Python 3.4
# 
# /r/dailyprogrammer Challenge #228 Easy - Letters in Alphabetical Order
# https://www.reddit.com/r/dailyprogrammer/comments/3h9pde/20150817_challenge_228_easy_letters_in/

from sys import argv

def readWords(source):
    w = []
    with open(source) as f:
        for line in f:
            w.append(line.strip())
    return w

def checkOrder(words):
    for w in words:
        if inOrder(w):
            print(w, "IN ORDER")
        elif revOrder(w):
            print(w, "REVERSE ORDER")
        else:
            print(w, "NOT IN ORDER")

def inOrder(w):
    return w == ''.join(sorted(w))

def revOrder(w):
    o = sorted(w)
    o.reverse()
    return w == ''.join(o)

if __name__ == "__main__":
    words = readWords(argv[1])
    checkOrder(words)