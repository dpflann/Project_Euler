# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# COLIN - 3 + 15 + 12 + 9 + `4 = 53 is the 983th name in the list. So COLIN = 938 x 53
#
# What is the total of all the name scores in the file?

def obtainNamesFromFile(aNamesFile):
  namesFile = open(aNamesFile, 'r')
  namesFileString = namesFile.read()
  namesFile.close()
  namesFileString = namesFileString.replace('"', '')
  names = namesFileString.split(',')
  return names

def letterValueGen(letter):
  yield letter
  yield (ord(letter) - ord('A') + 1)

def calculateNameScore(name, index):
  import string as s
  # { "A" : 1, "B" : 2, ..., "Z" : 1 }
  alphaIndexLookupTable = dict(map(letterValueGen, s.ascii_uppercase))
  score = reduce(lambda total, letter: total + alphaIndexLookupTable[letter], name, 0)
  score = score * (index + 1)
  return score

def totalNameScores():
  names = obtainNamesFromFile("names.txt")
  names.sort()
  totalScore = reduce(lambda total, i: total + calculateNameScore(names[i], i), range(len(names)), 0)
  return totalScore

def solve():
  print "The total of all the name scores in the file is %d." % totalNameScores()

if __name__ == '__main__':
  solve()
