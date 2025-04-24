from pathlib import Path

from common import *
from data import *

TOP_DELIMITER_LEFT = "---------- "
TOP_DELIMITER_RIGHT = " ----------\n"
BOTTOM_DELIMITER = "-------------------------------------------\n"

isTopDelimiter = lambda line : (TOP_DELIMITER_LEFT in line) and \
                               (TOP_DELIMITER_RIGHT in line)
isBottomDelimiter = lambda line: line == BOTTOM_DELIMITER

def parse(buffer):
  print(buffer)
  return

def getAverage():
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
  getAverage()