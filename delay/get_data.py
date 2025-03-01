from pathlib import Path

from common import *
from data import *

PRINT_AVERAGES = True

def getAverages():
  """This dictionary needs to be in the order of increasing TX power,
     as the exact order in which the data is organized in the dictionary
     will be used when displaying data across the x-axis.
  """
  averagesDict = {
    "No Encryption": {
      "0 dBm": None,
      "9 dBm": None,
      "20 dBm": None
    },
    "AES": {
      "0 dBm": None,
      "9 dBm": None,
      "20 dBm": None
    },
    "ASCON-128a": {
      "0 dBm": None,
      "9 dBm": None,
      "20 dBm": None
    },
    "ASCON-128": {
      "0 dBm": None,
      "9 dBm": None,
      "20 dBm": None
    }
  }

  standDevsDict = {
    "No Encryption": {
      "0 dBm": 0,
      "9 dBm": 0,
      "20 dBm": 0
    },
    "AES": {
      "0 dBm": 0,
      "9 dBm": 0,
      "20 dBm": 0
    },
    "ASCON-128a": {
      "0 dBm": 0,
      "9 dBm": 0,
      "20 dBm": 0
    },
    "ASCON-128": {
      "0 dBm": 0,
      "9 dBm": 0,
      "20 dBm": 0
    }
  }

  for cipher in THESIS_DELAY_AVERAGES.keys():
    for txPower in THESIS_DELAY_AVERAGES[cipher].keys():
      filepath = THESIS_DELAY_AVERAGES[cipher][txPower]

      if filepath != None:
        with filepath.open("r") as file:
          for line in file:
            if "Final Average Delay under" in line:
              if PRINT_AVERAGES:
                print(line)

              words = line.strip("\n").split(" ")
              if "No Encrypt" in line:
                # The final average is the 9th word (assuming 0 index) in the sentence.
                averagesDict[cipher][txPower] = float(words[9])
              else:
                # The final average is the 8th word (assuming 0 index) in the sentence.
                averagesDict[cipher][txPower] = float(words[8])

            elif "The Standard Deviation is:" in line:
              if PRINT_AVERAGES:
                print(line)

              stdStr = line.strip("\n").split(" ")[4]
              standDevsDict[cipher][txPower] = float(stdStr[0:len(stdStr)-1])

  return averagesDict, standDevsDict

if __name__ == "__main__":
  averagesDict, standDevsDict = getAverages()