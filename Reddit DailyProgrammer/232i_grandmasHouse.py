# Written for Python 3.4
# 
# /r/dailyprogrammer Challenge #232 Intermediate - Grandma's House
# https://www.reddit.com/r/dailyprogrammer/comments/3l61vx/20150916_challenge_232_intermediate_where_should/

import sys
import time
from math import sqrt
from operator import itemgetter

def readData(source):
    with open(source, 'r') as f:
        lines = int(f.readline())
        data = []
        for i in range(lines):
            d = f.readline()
            d = d.strip("()\n").split(',')
            data.append((float(d[0]), float(d[1])))
    return data

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def bruteForce(data):
    short = [data[0], data[1], distance(data[0], data[1])]
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            diff = distance(data[i], data[j])
            if diff < short[2]:
                short = [data[i], data[j], diff]
    return short

# Uses the recursive divide and conquer algorithm described here:
# https://en.wikipedia.org/wiki/Closest_pair_of_points_problem
def divideAndConquer(data):
    if len(data) <= 3:
        return bruteForce(data)

    mid = len(data) // 2
    left = divideAndConquer(data[:mid])
    right = divideAndConquer(data[mid:])
    minLR = min(left, right, key=itemgetter(2))

    close = [x for x in data if abs(x[0] - data[mid][0]) < minLR[2]]
    if len(close) > 1:
        minDivide = bruteForce(close)
    else:
        minDivide = [(float("inf"), float("inf")), (float("inf"), float("inf")), float("inf")]

    return min(minLR, minDivide, key=itemgetter(2))

if __name__ == "__main__":
    #data = sorted(readData(sys.argv[1]))
    #result = bruteForce(data)
    #print(result[0], result[1])
    print("N = 16")
    data = sorted(readData("232i_input_1.txt"))
    start = time.time()
    result = bruteForce(data)
    end = time.time()
    print("Brute force completed in {0:.3f} sec.".format(end-start))
    print(result)
    print()
    start = time.time()
    result = divideAndConquer(data)
    end = time.time()
    print("Divide and conquer completed in {0:.3f} sec.".format(end-start))
    print(result)

    print("\n\nN = 100")
    data = sorted(readData("232i_input_2.txt"))
    start = time.time()
    result = bruteForce(data)
    end = time.time()
    print("Brute force completed in {0:.3f} sec.".format(end-start))
    print(result)
    print()
    start = time.time()
    result = divideAndConquer(data)
    end = time.time()
    print("Divide and conquer completed in {0:.3f} sec.".format(end-start))
    print(result)

    print("\n\nN = 5000")
    data = sorted(readData("232i_input_3.txt"))
    start = time.time()
    result = bruteForce(data)
    end = time.time()
    print("Brute force completed in {0:.3f} sec.".format(end-start))
    print(result)
    print()
    start = time.time()
    result = divideAndConquer(data)
    end = time.time()
    print("Divide and conquer completed in {0:.3f} sec.".format(end-start))
    print(result)