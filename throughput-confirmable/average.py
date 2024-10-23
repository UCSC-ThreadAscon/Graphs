""" Calculates the average using ONLY the data from the FIRST 1000 TRIALS.
"""
import re
import os
import sys

from data import *

NUM_TRIALS = 1000

def getAverageThroughputs(filepath):
  averages = []
  with open(filepath, 'r') as file:
    for line in file:
      if "bytes/second, or" in line:
        print(line)

  # Only return the first NUM_TRIALS trials.
  return

""" https://stackoverflow.com/a/35833387/6621292
"""
def getFinalAverage(averages):
  listSum = 0
  for average in averages:
    listSum += average

    if (listSum == sys.float_info.max):
      raise OverflowError("Reach maxed float. Can't add anymore.")

  return listSum / len(averages)

def findFirstLine(expression, filepath):
  with open(filepath, 'r') as file:
    for line in file:
      if expression in line:
        return line
  raise Exception(f"Can't find expression '{expression}' in '{filepath}'.")

"""The lines of code and regular expression I used to remove ANSI escape
   sequences comes from:
   https://stackoverflow.com/a/14693789/6621292
"""
def removeAnsi(line):
  ansiEscapes = re.compile(
    br'(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])'
  )
  result = ansiEscapes.sub(b'', bytes(line, "utf-8"))
  return str(result, encoding="utf-8")

def writeFinalAverage(averageDelays, finalAverage, delayExpLog):
  line = findFirstLine("Cipher Suite:", delayExpLog)
  words = line.split(" ")
  cipher = removeAnsi(words[5]).replace('\n', '')

  # If "No" gets parsed, it's actually supposed to be "No Encrypt".
  # Since " " is used as a delimiter, the "Encrypt" word will be missed
  # during the parsing process.
  #
  if cipher == "No":
    cipher = "No Encrypt"

  line = findFirstLine("Max TX Power is:", delayExpLog)
  words = line.split(" ")
  txPower = words[7]

  outputFile = os.path.join(os.getcwd(), "final-averages", LOCATION, f"delay-final-average-FIRST-1000-{cipher}-{txPower}dbm.txt")

  with open(outputFile, "w") as file:
    file.write(f"Final Average Delay under {cipher} at {txPower} dBm: {finalAverage} us.\n")
    file.write("List of Average Delays used to create the Final Average:\n")

    trialNum = 1
    for average in averageDelays:
      file.write(f"Trial {trialNum}: {average} us")
      trialNum += 1
      if trialNum <= len(averageDelays):
        file.write("\n")
  return

def getAllAverages():
  for filesDict in THESIS_DELAY_LOGS.values():
    for logFile in filesDict.values():
      averages = getAverageThroughputs(logFile)
      finalAverage = getFinalAverage(averages)
      writeFinalAverage(averages, finalAverage, logFile)
  return

if __name__ == "__main__":
  getAverageThroughputs(THESIS_DELAY_LOGS["AES"]["20 dBm"])