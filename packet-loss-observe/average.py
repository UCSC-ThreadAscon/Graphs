""" Calculates the average using ONLY the data from the FIRST 1000 TRIALS.
"""
import re
import os
import sys

from data import *

NUM_TRIALS = 100

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

def getAveragePacketLosses(filepath):
  averages = []
  with open(filepath, 'r') as file:
    for line in file:
      if "Packet Loss Ratio:" in line:
        line = removeAnsi(line)
        words = line.split(" ")

        average = float(words[6])
        averages.append(average)

  # Only return the first NUM_TRIALS trials.
  return averages[0:NUM_TRIALS:]

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

def writeFinalAverage(averagePacketLossRatios, finalAverage, packetLossExpLog):
  line = findFirstLine("Cipher Suite:", packetLossExpLog)
  words = line.split(" ")
  cipher = removeAnsi(words[5]).replace('\n', '')

  # If "No" gets parsed, it's actually supposed to be "No Encrypt".
  # Since " " is used as a delimiter, the "Encrypt" word will be missed
  # during the parsing process.
  #
  if cipher == "No":
    cipher = "No Encrypt"

  line = findFirstLine("Max TX Power is:", packetLossExpLog)
  words = line.split(" ")
  txPower = words[7]

  outputFile = os.path.join(os.getcwd(), "final-averages", f"pl-con-final-average-{cipher}-{txPower}dbm.txt")

  with open(outputFile, "w") as file:
    file.write(f"Final Average Packet Loss (Confirmable) under {cipher} at {txPower} dBm: {finalAverage} %.\n")
    file.write("List of Average (Confirmable) Packet Loss Percentages used to create the Final Average:\n")

    trialNum = 1
    for average in averagePacketLossRatios:
      file.write(f"Trial {trialNum}: {average} %")
      trialNum += 1
      if trialNum <= len(averagePacketLossRatios):
        file.write("\n")
  return

def getAllAverages():
  for filesDict in THESIS_PL_CON_LOGS.values():
    for logFile in filesDict.values():
      if logFile != None:
        averages = getAveragePacketLosses(logFile)
        finalAverage = getFinalAverage(averages)
        writeFinalAverage(averages, finalAverage, logFile)
  return

if __name__ == "__main__":
  getAllAverages()