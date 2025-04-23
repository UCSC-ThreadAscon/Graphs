import sys
import csv

from common import *
from data import *

# 183 minutes expressed as milliseconds.
EXPERIMENT_DURATION_MS = (183 * 60 * 1000)

""" TODO: Determine when the device gets powered on, and print out the timestamp
          and current the moment it powers on.
"""
def getAvgUa(filename):
  tsPowerOn = None

  with open(filename) as file:
    for row in csv.DictReader(file):
      timestamp = float(row["Timestamp(ms)"])
      uA = float(row["Current(uA)"])

      if tsPowerOn is not None:
        # Only measure power consumption for `EXPERIMENT_DURATION_MS` milliseconds
        # after the device first powers on.
        #
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
  return

if __name__ == "__main__":
  getAvgUa(THESIS_ENERGY_CSV["AES"]["20 dBm"])