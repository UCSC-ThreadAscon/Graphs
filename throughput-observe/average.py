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

def writeFinalAverage(averages, finalAverage, delayExpLog):
  line = findFirstLine("Cipher Suite:", delayExpLog)
  words = line.split(" ")
  cipher = removeAnsi(words[5]).replace('\n', '')

  if cipher == "No":
    cipher = "No Encrypt"

  line = findFirstLine("Max TX Power is:", delayExpLog)
  words = line.split(" ")
  txPower = words[7]

  outputFile = os.path.join(os.getcwd(), "final-averages", f"tp-con-final-average-{cipher}-{txPower}dbm.txt")

  with open(outputFile, "w") as file:
    file.write(f"Final Average Throughput (Observe) under {cipher} at {txPower} dBm: {finalAverage} bytes/second.\n")
    file.write("List of Average Throughputs (Observe) used to create the Final Average:\n")

    trialNum = 1
    for average in averages:
      file.write(f"Trial {trialNum}: {average} bytes/second")
      trialNum += 1
      if trialNum <= len(averages):
        file.write("\n")
  return

if __name__ == "__main__":
  averages = getAverages(THESIS_TP_OBSERVE_LOGS["ASCON-128"]["20 dBm"])
  finalAverage = getFinalAverage(averages)

  print(averages)
  print(f"The final average for ASCON-128 20 dBm is {finalAverage} bytes/second.")