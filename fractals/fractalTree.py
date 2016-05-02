"""
A fractal tree builder.
"""
# Modify the recursive tree program using one or all of the following ideas:

# Modify the thickness of the branches so that as the branchLen gets smaller,
#   the line gets thinner.
# Modify the color of the branches so that as the branchLen gets very short
#   it is colored like a leaf.
# Modify the angle used in turning the turtle so that at each branch point
#   the angle is selected at random in some range. For example choose the
#   angle between 15 and 45 degrees. Play around to see what looks good.
# Modify the branchLen recursively so that instead of always subtracting the
#   same amount you subtract a random amount in some range.

import turtle
import random

def tree(branchLen, t):
    if branchLen > 5:
        if branchLen >= 13:
            t.color("burlywood3")
        else:
            t.color("green")
        t.width(branchLen // 7)
        t.forward(branchLen)
        r = random.randrange(15, 35)
        l = random.randrange(15, 35)
        t.right(r)
        tree(branchLen - random.randrange(5, 20), t)
        t.left(r+l)
        tree(branchLen - random.randrange(5, 20), t)
        t.right(l)
        if branchLen >= 13:
            t.color("burlywood3")
        else:
            t.color("green")
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    #t.color("brown")
    tree(85, t)
    myWin.exitonclick()

main()
