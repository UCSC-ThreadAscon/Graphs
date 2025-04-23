import sys
import csv

from common import *
from data import *

MA_WAKEUP_MINIMUM = 2
UA_WAKEUP_MINIMUM = MA_WAKEUP_MINIMUM * 1000

""" TODO: Print the first 1000 entries of the PPK2 file.
"""

def getAvgUa(filename):
  with open(filename) as file:
    reader = csv.DictReader(file)

    i = 0
    for row in reader:
      if i >= 100:
        break
      else:
        timestamp = float(row["Timestamp(ms)"])
        uA = float(row["Current(uA)"])
        print(f"At {timestamp} ms current was {uA} uA.")
      i += 1

  return

if __name__ == "__main__":
  getAvgUa(THESIS_ENERGY_CSV["AES"]["20 dBm"])