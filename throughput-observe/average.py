import re
import os
import sys

from data import *

def getAverages(filepaths):
  averages = []

  for filepath in filepaths:
    with open(filepath, 'r') as file:
      for line in file:
        if "bytes/second, or" in line:
          words = line.split(" ")
          average = float(words[3])
          averages.append(average)

  return averages

""" https://stackoverflow.com/a/35833387/6621292
"""
def getFinalAverage(averages):
  listSum = 0
  for average in averages:
    listSum += average

    if (listSum == sys.float_info.max):
      raise OverflowError("Reach maxed float. Can't add anymore.")

  return listSum / len(averages)

if __name__ == "__main__":
  averages = getAverages(THESIS_TP_OBSERVE_LOGS["ASCON-128"]["20 dBm"])
  finalAverage = getFinalAverage(averages)

  print(averages)
  print(f"The final average for ASCON-128 20 dBm is {finalAverage} bytes/second.")