#!/usr/bin/python3
#
# Written for use with Python 3.4
#
# /r/dailyprogrammer Challenge #190 Easy - Webscraping sentiments
# https://www.reddit.com/r/dailyprogrammer/comments/2nauiv/20141124_challenge_190_easy_webscraping_sentiments/

import sys
import urllib.request as url

# Provided keywords from the challenge
happy = ['love','loved','like','liked','awesome','amazing','good','great','excellent']
sad = ['hate','hated','dislike','disliked','awful','terrible','bad','painful','worst']

template = "https://plus.googleapis.com/u/0/_/widget/render/comments?first_party_property=YOUTUBE&href="
input = sys.argv[1]

opener = url.urlopen(template + input)
source = str(opener.read())

cmts = []
pos = 0
# str.find() returns -1 if substring not found
while True:
  cmtStart = source.find('<div class="Ct">', pos)
  if cmtStart == -1:
    break
  cmtEnd = source.find('</div>', cmtStart)
  cmts.append(source[cmtStart+16:cmtEnd])
  pos = cmtEnd

positive = 0
negative = 0
for i in cmts:
  for j in happy:
    if j in i:
      positive += 1
      break
  for j in sad:
    if j in i:
      negative += 1
      break

print("Analysis of {0} comments for the video at {1}:".format(len(cmts), input))
print("Positive: {0}\nNegative: {1}".format(positive, negative))

