#!/usr/bin/python
# Written for Python 3.4
# 
# The Coding Dead
# /r/dailyprogrammer Challege #186 Intermediate The Coding Dead
# https://www.reddit.com/r/dailyprogrammer/comments/2kwfqr/10312014_challenge_186_special_code_or_treat/
# Simulates a map randomly populated with Zombies, Hunters, Victims

# Load modules
import sys
import random


##############################
# Prints the map in a nicely formatted way
# Takes a type and position list
def printMap(type, pos):
  map = [x[:] for x in [["-"]*mapDim]*mapDim]
  
  for i in range(len(type)):
    #print("For index {0}, type is {1} and position is {2}.".format(i, type[i], pos[i]))
    map[pos[i][0]][pos[i][1]] = type[i]
  
  for i in map:
    for j in i:
      print(j, end="")
    print()

##############################
# Initialize the map
def initialize():
  initType = []
  initPos = []
  
  # Create a list of random positions
  pos = []
  while len(pos) < (zomb+hunt+vict):
    num = random.randrange(totSpaces)
    if num not in pos:
      pos.append(num)
  
  i = 0
  while i < zomb:
    initType.append("Z")
    initPos.append((pos[i]//mapDim, pos[i]%mapDim))
    i += 1
  while i < (zomb+hunt):
    initType.append("H")
    initPos.append((pos[i]//mapDim, pos[i]%mapDim))
    i += 1
  while i < (zomb+hunt+vict):
    initType.append("V")
    initPos.append((pos[i]//mapDim, pos[i]%mapDim))
    i += 1
  
  print("The initial map is:")
  printMap(initType, initPos)
  print("$$$$$$$$$$$$$$$$$$$$")
  
  return (initType, initPos)

##############################
# Move the creatures
def moveCreatures(type, pos):
  nextType = []
  nextPos = []
  for i in range(len(type)):
    print("\nCreature {0} is {1} at {2}.".format(i, type[i], pos[i]))
    if type[i] == "V":
      # Victims only move if zombie nearby
      threat = checkNearby(type, pos, i)
      print("There are {0} threats nearby.".format(len(threat)))
      if threat != []:
        dir = random.randrange(8)
        newPos = move(dir, pos, i)
        if newPos not in nextPos:
          nextPos.append(newPos)
        else:
          nextPos.append(pos[i])
        nextType.append("V")
        print("New position: {0}".format(nextPos[-1]))
      else:
        nextPos.append(pos[i])
        nextType.append("V")
    elif type[i] == "H":
      dir = random.randrange(8)
      newPos = move(dir, pos, i)
      if newPos not in nextPos:
        nextPos.append(newPos)
      else:
        nextPos.append(pos[i])
      nextType.append("H")
      print("New position: {0}".format(nextPos[-1]))
    else:
      dir = random.randrange(0, 8, 2)
      newPos = move(dir, pos, i)
      if newPos not in nextPos:
        nextPos.append(newPos)
      else:
        nextPos.append(pos[i])
      nextType.append("Z")
      print("New position: {0}".format(nextPos[-1]))
  return (nextType, nextPos)

##############################
# Generalized movement
# Takes a direction, the full position list and the index of the creature
# 0 = up - (-1, 0)
# 1 = up right - (-1, 1)
# 2 = right - (0, 1)
# 3 = down right - (1, 1)
# 4 = down - (1, 0)
# 5 = down left - (1, -1)
# 6 = left - (0, -1)
# 7 - up left - (-1, -1)
def move(dir, pos, i):
  if dir == 0:
    print("Attempting to move up.")
    if pos[i][0] > 0: # Check we're not at the top of the map already
      newPos = (pos[i][0]-1, pos[i][1])
      if newPos not in pos:
        return newPos
      else:
        return pos[i]
    else:
      return pos[i]
  elif dir == 1:
    print("Attempting to move up-right.")
    if (pos[i][0] > 0) and (pos[i][1] < mapDim-1):
      newPos = (pos[i][0]-1, pos[i][1]+1)
      if newPos not in pos:
        return newPos
      else:
        return pos[i]
    else:
      return pos[i]
  elif dir == 2:
    print("Attempting to move right.")
    if pos[i][1] < mapDim-1:
      newPos = (pos[i][0], pos[i][1]+1)
      if newPos not in pos:
        return newPos
      else:
        return pos[i]
    else:
      return pos[i]
  elif dir == 3:
    print("Attempting to move down-right.")
    if (pos[i][0] < mapDim-1) and (pos[i][1] < mapDim-1):
      newPos = (pos[i][0]+1, pos[i][1]+1)
      if newPos not in pos:
        return newPos
      else:
        return pos[i]
    else:
      return pos[i]
  elif dir == 4:
    print("Attempting to move down.")
    if pos[i][0] < mapDim-1:
      newPos = (pos[i][0]+1, pos[i][1])
      if newPos not in pos:
        return newPos
      else:
        return pos[i]
    else:
      return pos[i]
  elif dir == 5:
    print("Attempting to move down-left.")
    if (pos[i][0] < mapDim-1) and (pos[i][1] > 0):
      newPos = (pos[i][0]+1, pos[i][1]-1)
      if newPos not in pos:
        return newPos
      else:
        return pos[i]
    else:
      return pos[i]
  elif dir == 6:
    print("Attempting to move left.")
    if pos[i][1] > 0:
      newPos = (pos[i][0], pos[i][1]-1)
      if newPos not in pos:
        return newPos
      else:
        return pos[i]
    else:
      return pos[i]
  elif dir == 7:
    print("Attempting to move up-left.")
    if (pos[i][0] > 0) and (pos[i][1] > 0):
      newPos = (pos[i][0]-1, pos[i][1]-1)
      if newPos not in pos:
        return newPos
      else:
        return pos[i]
    else:
      return pos[i]

##############################
# Check around a creature to see if there is anyone next to them
# For victims and hunters check all 8 spaces for a zombie
# For zombies check 4 adjacent spaces for victim or hunter
# Returns a list of indices with nearby threats/prey
def checkNearby(type, pos, ind):
  check8 = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
  check4 = [(-1,0), (0,-1), (1,0), (0,1)]
  
  nearby = []
  if (type[ind] == "H") or (type[ind] == "V"):
    for i in check8:
      if (pos[ind][0]+i[0], pos[ind][1]+i[1]) in pos:
        j = pos.index((pos[ind][0]+i[0], pos[ind][1]+i[1]))
        if type[j] == "Z":
          nearby.append(j)
  else:
    for i in check4:
      if (pos[ind][0]+i[0], pos[ind][1]+i[1]) in pos:
        j = pos.index((pos[ind][0]+i[0], pos[ind][1]+i[1]))
        if (type[j] == "H") or (type[j] == "V"):
          nearby.append(j)
  
  return nearby

##############################
# Hunters slay zombies
def slayZomb(type, pos):
  newType = list(type)
  newPos  = list(pos)
  
  global slay1
  slay1.append(0)
  global slay2
  slay2.append(0)
  
  for i in range(len(type)):
    if type[i] == "H":
      print("\nHunter at {0}...".format(pos[i]))
      targets = checkNearby(newType, newPos, newPos.index((pos[i][0], pos[i][1])) )
      targets.sort()
      print("has {0} targets.".format(len(targets)))
      if len(targets) == 1:
        print("Slayed zombie at {0}.".format(newPos[targets[0]]))
        newType.pop(targets[0])
        newPos.pop(targets[0])
        slay1[-1] += 1
      elif len(targets) == 2:
        print("Slayed zombies at {0} and {1}.".format(newPos[targets[0]], newPos[targets[1]]))
        newType.pop(targets[1])
        newPos.pop(targets[1])
        newType.pop(targets[0])
        newPos.pop(targets[0])
        slay2[-1] += 1
      elif len(targets) > 2:
        hit = [None, None]
        hit[0] = targets[random.randrange(len(targets))]
        hit[1] = targets[random.randrange(len(targets))]
        while hit[1] == hit[0]:
          hit[1] = targets[random.randrange(len(targets))]
        hit.sort()
        print("Slayed zombies at {0} and {1}.".format(newPos[hit[0]], newPos[hit[1]]))
        newType.pop(hit[1])
        newPos.pop(hit[1])
        newType.pop(hit[0])
        newPos.pop(hit[0])
        slay2[-1] += 1
  
  return (newType, newPos)

##############################
# Zombies bite victims or hunters
# People bit immediately turn into zombies
def bite(type, pos):
  newType = list(type)
  newPos  = list(pos)
  
  global biteH
  biteH.append(0)
  global biteV
  biteV.append(0)
  
  for i in range(len(type)):
    if type[i] == "Z":
      print("\nZombie at {0}...".format(pos[i]))
      targets = checkNearby(newType, newPos, i)
      targets.sort()
      print("has {0} targets.".format(len(targets)))
      if len(targets) == 1:
        print("Bit {0} at {1}.".format(type[targets[0]], pos[targets[0]]))
        if type[targets[0]] == "H":
          biteH[-1] += 1
        else:
          biteV[-1] += 1
        newType[targets[0]] = "Z"
      elif len(targets) > 1:
        atk = targets[ random.randrange(len(targets)) ]
        print("Bit {0} at {1}.".format(type[atk], pos[atk]))
        if type[atk] == "H":
          biteH[-1] += 1
        else:
          biteV[-1] += 1
        newType[atk] = "Z"
  
  return (newType, newPos)


##############################
# Set up variables to be used throughout
mapDim = 20
totSpaces = mapDim**2

# Set a seed for testing purposes
random.seed(12345)

zomb  = int(sys.argv[1])
hunt  = int(sys.argv[2])
vict  = int(sys.argv[3])
ticks = int(sys.argv[4])
# Figure out more about Python error throwing and update this.
if (zomb+hunt+vict) > totSpaces:
  print("You cannot have more creatures than available spaces on the map!")

##############################
# Set up data reporting variables
zMove = [0]
hMove = [0]
vMove = [0]

numZ = [zomb]
numH = [hunt]
numV = [vict]

slay1 = [0]
slay2 = [0]

biteH = [0]
biteV = [0]

##############################
# Run the main portion of the code
creatType, creatPos = initialize()
for i in range(1, ticks+1):
  intermedType, intermedPos = moveCreatures(creatType, creatPos)
  print("\nAfter moving at tick {0} the map is:".format(i))
  printMap(intermedType, intermedPos)
  
  slayType, slayPos = slayZomb(intermedType, intermedPos)
  print("\nAfter slaying zombies at tick {0} the map is:".format(i))
  printMap(slayType, slayPos)
  
  biteType, bitePos = bite(slayType, slayPos)
  print("\nAfter zombies bite at tick {0} the map is:".format(i))
  printMap(biteType, bitePos)



