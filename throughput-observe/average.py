import os
import sys

from data import *
from common import *

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

def writeFinalAverage(averages, finalAverage, cipher, txPower):
  outputFile = os.path.join(os.getcwd(),
                            "final-averages", 
                            f"tp-observe-final-average-{cipher}-{txPower.split()[0]}dbm.txt")

  with open(outputFile, "w") as file:
    file.write(f"Final Average Throughput (Observe) under {cipher} at {txPower}: {finalAverage} bytes/second.\n")
    file.write("List of Average Throughputs (Observe) used to create the Final Average:\n")

    trialNum = 1
    for average in averages:
      file.write(f"Trial {trialNum}: {average} bytes/second")
      trialNum += 1
      if trialNum <= len(averages):
        file.write("\n")
  return

def getAllAverages():
  for cipher in CIPHERS:
    for txPower in TX_POWERS:
      logsList = THESIS_TP_OBSERVE_LOGS[cipher][txPower]

      if len(logsList) > 0:
        averages = getAverages(logsList)
        finalAverage = getFinalAverage(averages)
        writeFinalAverage(averages, finalAverage, cipher, txPower)
  return

if __name__ == "__main__":
  getAllAverages()