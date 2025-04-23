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

def getSamples(filepath):
  uAList = []
  tsPowerOn = None

  with open(filepath) as file:
    for row in csv.DictReader(file):
      timestamp = float(row["Timestamp(ms)"])
      uA = float(row["Current(uA)"])

      if tsPowerOn is not None:
        # Only measure power consumption for `EXPERIMENT_DURATION_MS` milliseconds
        # after the device first powers on.
        #
        uAList.append(uA)

        if len(uAList) >= sys.maxsize:
          raise OverflowError("The list is too big.")

        elapsed = timestamp - tsPowerOn
        if (elapsed >= EXPERIMENT_DURATION_MS):
          print(f"Stop post-processing @ {timestamp} ms with current {uA} uA.")
          break
      else:
        # When the ESP32 is powered off, the power consumption is at nA.
        # The moment the ESP32 is powered on, the power consumption will increase
        # from nA scale to uA/mA scale.
        #
        # Thus, to detect when the ESP32 is powered on, we look for the first spike
        # in power consumption that was recorded by the PPK2.
        #
        if uA >= 1:
          tsPowerOn = timestamp
          print(f"Device power on detected @ {timestamp} ms with current {uA} uA.")

  return uAList

""" TODO: Calculate the average given the list of samples.
"""
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

avgUa = lambda filepath : getAvgUa(getSamples(filepath))
avgMa = lambda filepath : uAtoMa(avgUa(filepath))
avgMah = lambda filepath : mAtoMah(avgMa(filepath))

if __name__ == "__main__":
  print(avgMah(THESIS_ENERGY_CSV["AES"]["20 dBm"]))

  # print(getAvgUa([100, math.inf, 100]))
  # print(getSamples(THESIS_ENERGY_CSV["AES"]["20 dBm"]))