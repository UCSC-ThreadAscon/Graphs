""" RESOURCES UTILIZED:
    ------------------
    https://stackoverflow.com/a/35833387/6621292
    https://electronics.stackexchange.com/a/107078
    https://docs.python.org/3/library/csv.html
"""
import sys
import csv
import math

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

def getSamples(filepath):
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
        if uA >= UA_WAKEUP_MINIMUM:
          uAWakeupList.append(uA)

        if len(uAList) >= sys.maxsize:
          raise OverflowError("The list is too big.")

        elapsed = timestamp - tsPowerOn
        if (elapsed >= EXPERIMENT_DURATION_MS):
          print(f"Stop post-processing @ {timestamp} ms with current {uA} uA.")
          break

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

def printAvgs(cipher, txPower):
  filepath = None
  uAList = getSamples(filepath)
  avgUa = getAvgUa(uAList)
  avgMa = uAtoMa(avgUa)
  avgMah = mAtoMah(avgMa)

  print(f"---------- {cipher} {txPower} ----------")
  print(f"The average uA, deep sleep included, is {avgUa} uA.")
  print(f"The average mA, deep sleep included, is {avgMa} mA.")
  print(f"The average mAh, deep sleep included, is {avgMah} mAh.")
  print("-------------------------------------------")
  return

if __name__ == "__main__":
  printAllAvgs()