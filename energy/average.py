import sys
import csv
import math

from common import *
from data import *

minToSec = lambda min : min * 60
secToMs = lambda sec : sec * 1000
minToMs = lambda min : secToMs(minToSec(min))
minToHrs = lambda min : min / 60

EXPERIMENT_DURATION_MINUTES = 183
EXPERIMENT_DURATION_MS = minToMs(EXPERIMENT_DURATION_MINUTES)
EXPERIMENT_DURATION_HRS = minToHrs(EXPERIMENT_DURATION_MINUTES)

uAtoMa = lambda uA : uA * 0.001
mAtoMah = lambda mA : mA * EXPERIMENT_DURATION_HRS
mAtoUa = lambda mA : mA * 1000

UA_WAKEUP_MINIMUM = 9

""" TODO: Instead of choosing whether or not to only count average for wakeups or not,
          why not do both at the same time?
"""

def getSamples(filepath):
  uAList = []
  uAWakeupList = []
  tsPowerOn = None

  with open(filepath) as file:
    for row in csv.DictReader(file):
      timestamp = float(row["Timestamp(ms)"])
      uA = float(row["Current(uA)"])

      if (tsPowerOn is None) and (uA >= 1): # Power on spike of ESP32-H2.
        tsPowerOn = timestamp
        print(f"Device power on detected @ {timestamp} ms with current {uA} uA.")

      if tsPowerOn is not None:
        uAList.append(uA)
        if uA >= UA_WAKEUP_MINIMUM:
          uAWakeupList.append(uA)

        if len(uAList) >= sys.maxsize:
          raise OverflowError("The list is too big.")

        elapsed = timestamp - tsPowerOn
        if (elapsed >= EXPERIMENT_DURATION_MS):
          print(f"Stop post-processing @ {timestamp} ms with current {uA} uA.")
          break

  return uAList, uAWakeupList

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

def getAllAvgs(cipher, txPower):
  filepath = THESIS_ENERGY_CSV[cipher][txPower]
  uAList, uAWakeupList = getSamples(filepath)

  avgUa = getAvgUa(uAList)
  avgMa = uAtoMa(avgUa)
  avgMah = mAtoMah(avgMa)

  avgUaWakeup = getAvgUa(uAWakeupList)
  avgMaWakeup = uAtoMa(avgUaWakeup)
  avgMahWakeup = mAtoMah(avgMaWakeup)

  print(f" ---------- {cipher} {txPower} ----------")
  print(f"The average uA, deep sleep included, is {avgUa} uA.")
  print(f"The average mA, deep sleep included, is {avgMa} mA.")
  print(f"The average mAh, deep sleep included, is {avgMah} mAh.")
  print(f"The average uA on wakeup is {avgUaWakeup} uA.")
  print(f"The average mA on wakeup is {avgMaWakeup} mA.")
  print(f"The average mAh on wakeup is {avgMahWakeup} mAh.")
  print("-------------------------------------------")
  return

if __name__ == "__main__":
  getAllAvgs("AES", "20 dBm")

  # print(getAvgUa([100, math.inf, 100]))
  # print(getSamples(THESIS_ENERGY_CSV["AES"]["20 dBm"]))