import sys
import csv

from common import *
from data import *

minToSec = lambda min : min * 60
secToMs = lambda sec : sec * 1000
minToMs = lambda min : secToMs(minToSec(min))

EXPERIMENT_DURATION_MINUTES = 183
EXPERIMENT_DURATION_MS = minToMs(EXPERIMENT_DURATION_MINUTES)

""" TODO: Determine when the device gets powered on, and print out the timestamp
          and current the moment it powers on.
"""
def getUaList(filename):
  uAList = []
  tsPowerOn = None

  with open(filename) as file:
    for row in csv.DictReader(file):
      timestamp = float(row["Timestamp(ms)"])
      uA = float(row["Current(uA)"])

      if tsPowerOn is not None:
        # Only measure power consumption for `EXPERIMENT_DURATION_MS` milliseconds
        # after the device first powers on.
        #
        uAList.append(uA)

        elapsed = timestamp - tsPowerOn
        if (elapsed >= EXPERIMENT_DURATION_MS):
          print(f"Stop post-porcessing @ {timestamp} ms with current {uA} uA.")
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

if __name__ == "__main__":
  getAvgUa(THESIS_ENERGY_CSV["AES"]["20 dBm"])