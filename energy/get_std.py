from pathlib import Path

from common import *
from data import *

TOP_DELIMITER_LEFT = "---------- "
TOP_DELIMITER_RIGHT = " ----------\n"
BOTTOM_DELIMITER = "-------------------------------------------\n"

isTopDelimiter = lambda line : (TOP_DELIMITER_LEFT in line) and \
                               (TOP_DELIMITER_RIGHT in line)
isBottomDelimiter = lambda line: line == BOTTOM_DELIMITER

def getIndepVars(line):
  cipher = None
  txPower = None

  if "No Encryption" in line:
    cipher = "No Encryption"
  elif "AES" in line:
    cipher = "AES"
  elif "ASCON-128a" in line:
    cipher = "ASCON-128a"
  elif "ASCON-128" in line:
    cipher = "ASCON-128"
  elif "AsconAead128" in line:
    cipher = "AsconAead128"

  if "20 dBm" in line:
    txPower = "20 dBm"
  elif "9 dBm" in line:
    txPower = "9 dBm"
  elif "0 dBm" in line:
    txPower = "0 dBm"

  return cipher, txPower

def parse(buffer):
  print(buffer)
  return

def getStds():
  stdDict = initEmptyDict()

  with open(AVERAGES_TEXT_FILE, "r") as file:
    buffer = []
    for line in file:
      if isTopDelimiter(line):
        buffer = []

      buffer.append(line)

      if isBottomDelimiter(line):
        parse(buffer)

  return

if __name__ == "__main__":
  print(getStds())