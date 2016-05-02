"""
A recursive fractal tree builder.
"""
# Modify the thickness of the branches so that as the branchLen gets smaller,
#   the line gets thinner.
# Modify the color of the branches so that as the branchLen gets very short
#   it is colored like a leaf.
# Modify the angle used in turning the turtle so that at each branch point
#   the angle is selected at random in some range. For example choose the
#   angle between 15 and 45 degrees. Play around to see what looks good.
# Modify the branchLen recursively so that instead of always subtracting the
#   same amount you subtract a random amount in some range.

import sys
import math
import random

import svgwrite

# Needed to define each branch of the tree:
# starting point
# branch length
# branch angle

# Given start = (x, y), length = r, angle = theta
# x2 = x + r * cos(theta)
# y2 = y + r * sin(theta)

def build_tree(start, branch_len, angle):
    """
    A recursive function to build a fractal tree.

    Input:
    start - (x, y) tuple giving the starting point of the tree
    branch_len - the length of this branch of the tree

    Output:
    tree - list of (x1, y1, x2, y2) defining the line segments of this tree
    """
    if branch_len <= 5:
        return []
    else:
        tree = []

        x_end = start[0] + (branch_len * math.cos(math.radians(angle)))
        y_end = start[1] + (branch_len * math.sin(math.radians(angle)))
        tree.append((start[0], start[1], x_end, y_end))

        # build the right branch
        right_angle = angle - 45
        right_branch_len = branch_len - 20
        tree += build_tree((x_end, y_end), right_branch_len, right_angle)

        # build the left branch
        left_angle = angle + 45
        left_branch_len = branch_len - 20
        tree += build_tree((x_end, y_end), left_branch_len, left_angle)

        return tree

def tree_normalize(tree):
    """
    Takes a list of line segments defining a tree and normalizes them by 
    making all coordinates positive.
    """
    # Find the minimum x and y values
    x_vals = [(i[0], i[2]) for i in tree]
    x_vals = [item for sublist in x_vals for item in sublist]
    y_vals = [(i[1], i[3]) for i in tree]
    y_vals = [item for sublist in y_vals for item in sublist]

    x_shift = abs(min(x_vals))
    y_shift = abs(min(y_vals))

    # Add the shift values to each point
    new_tree = []
    for line in tree:
        new_tree.append((
            line[0] + x_shift,
            line[1] + y_shift,
            line[2] + x_shift,
            line[3] + y_shift
            ))
    return new_tree

def write_tree(tree, filename):
    """
    Takes a list of line segments defining a tree and writes them to an SVG file.
    """
    tree = tree_normalize(tree)
    dwg = svgwrite.Drawing(filename=filename)

    # Add each branch to the drawing
    # TODO: vary line width as a function of branch length
    for branch in tree:
        dwg.add(dwg.line(start=branch[:2], end=branch[2:], stroke="black"))

    # Save the drawing
    dwg.save()

# def tree(branchLen, t):
#     if branchLen > 5:
#         if branchLen >= 13:
#             t.color("burlywood3")
#         else:
#             t.color("green")
#         t.width(branchLen // 7)
#         t.forward(branchLen)
#         r = random.randrange(15, 35)
#         l = random.randrange(15, 35)
#         t.right(r)
#         tree(branchLen - random.randrange(5, 20), t)
#         t.left(r+l)
#         tree(branchLen - random.randrange(5, 20), t)
#         t.right(l)
#         if branchLen >= 13:
#             t.color("burlywood3")
#         else:
#             t.color("green")
#         t.backward(branchLen)

# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(200)
#     t.down()
#     #t.color("brown")
#     tree(85, t)
#     myWin.exitonclick()

if __name__ == "__main__":
    TREE = build_tree((0, 0), 80, 270)
    for line in TREE:
        print(line)
    write_tree(TREE, "test.svg")

