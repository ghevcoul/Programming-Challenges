# Written for Python 3.4
# 
# /r/dailyprogrammer Challenge #236 Hard - Balancing Chemical Equations
# https://www.reddit.com/r/dailyprogrammer/comments/3oz82g/20151016_challenge_236_hard_balancing_chemical/

import sys
import re
from string import ascii_lowercase, ascii_uppercase, digits
import sympy

def readInput():
    s = input("What equation would you like balanced?\n")
    return s

def parseEquation(eq):
    lhs, rhs = re.split("\s*->\s*", eq)
    p =  {
        "reac":re.split("\s*\+\s*", lhs), 
        "prod":re.split("\s*\+\s*", rhs)
    }
    for i in ["reac", "prod"]:
        s = []
        for j in p[i]:
            d, elem, num = {}, [], []
            for c in j:
                if c in ascii_uppercase:
                    if len(elem) != 0:
                        if len(num) == 0:
                            d[''.join(elem)] = 1
                        else:
                            d[''.join(elem)] = int(''.join(num))
                        elem, num = [], []
                    elem.append(c)
                elif c in ascii_lowercase:
                    elem.append(c)
                elif c in digits:
                    num.append(c)
            if len(num) == 0:
                d[''.join(elem)] = 1
            else:
                d[''.join(elem)] = int(''.join(num))
            s.append((j, d))
        p[i] = s
    return p

def buildMatrix(p):
    # Compile the list of elements and check that they match 
    # between the reactants and products
    elems = []
    for i in ["reac", "prod"]:
        e = []
        for j in p[i]:
            e += list(j[1].keys())
        elems.append(set(e))
    if elems[0] != elems[1]:
        sys.exit("Elements in reactants and products do not match!")

    mat = []
    for e in elems[0]:
        r = []
        for j in p["reac"]:
            try:
                r.append(j[1][e])
            except KeyError:
                r.append(0)
        for j in p["prod"]:
            try:
                r.append(-1 * j[1][e])
            except KeyError:
                r.append(0)
        mat.append(r)
    return mat

def printResult(p, c):
    if min(c[0]) < 1:
        scale = 1/min(c[0])
    else:
        scale = 1
    
    res = []
    x = 0
    for i in range(len(p["reac"])):
        n = c[0][x]*scale
        if n == 1:
            res.append(p["reac"][i][0])
        else:
            res.append("{0}{1}".format(n, p["reac"][i][0]))
        if i < len(p["reac"])-1:
            res.append("+")
        x += 1
    res.append("->")
    for i in range(len(p["prod"])):
        n = c[0][x]*scale
        if n == 1:
            res.append(p["prod"][i][0])
        else:
            res.append("{0}{1}".format(c[0][x]*scale, p["prod"][i][0]))
        if i < len(p["prod"])-1:
            res.append("+")
        x += 1
    print("\n")
    print(" ".join(res))


def balanceEquation():
    equation = readInput()
    peq = parseEquation(equation)
    coeffs = sympy.Matrix(buildMatrix(peq)).nullspace()
    printResult(peq, coeffs)

if __name__ == "__main__":
    balanceEquation()