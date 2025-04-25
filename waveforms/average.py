""" RESOURCES UTILIZED:
    ------------------
    https://stackoverflow.com/a/35833387/6621292
    https://electronics.stackexchange.com/a/107078
    https://docs.python.org/3/library/csv.html
"""
from pathlib import Path
import sys
import csv
import math

CSV_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "waveforms", "csv")

uAtoMa = lambda uA : uA * 0.001
mAtoUa = lambda mA : mA * 1000

UA_WAKEUP_MINIMUM = 9

def getSamples(filepath):
  uAWakeupList = []

  with open(filepath) as file:
    for row in csv.DictReader(file):
      uA = float(row["Current(uA)"])
      if uA >= UA_WAKEUP_MINIMUM:
        uAWakeupList.append(uA)

      if len(uAWakeupList) >= sys.maxsize:
        raise OverflowError("The list is too big.")

  return uAWakeupList

def getAvgUa(samples):
  length = len(samples)
  accumulator = 0

  for uA in samples:
    accumulator += uA
    if (accumulator == sys.float_info.max) or \
       (accumulator == math.inf):
      raise OverflowError("Reach maxed float. Can't add anymore.")

  average = accumulator / length
  return average

def printAvgs(filepath, cipher, txPower):
  uAList = getSamples(filepath)
  avgUa = getAvgUa(uAList)
  avgMa = uAtoMa(avgUa)

  print(f"---------- {cipher} {txPower} ----------")
  print(f"The average uA, deep sleep included, is {avgUa} uA.")
  print(f"The average mA, deep sleep included, is {avgMa} mA.")
  print("-------------------------------------------")
  return

if __name__ == "__main__":
  printAvgs(Path(CSV_PATH, "AES-20dbm-last-waveform.csv"),
               "AES", "20 dBm")

  printAvgs(Path(CSV_PATH, "NoEncrypt-20dbm-last-waveform.csv"),
               "No Encryption", "20 dBm")

  printAvgs(Path(CSV_PATH, "LibAscon-128a-20dbm-last-waveform.csv"),
               "ASCON-128a", "20 dBm")

  printAvgs(Path(CSV_PATH, "LibAscon-128-20dbm-last-waveform.csv"),
               "ASCON-128", "20 dBm")