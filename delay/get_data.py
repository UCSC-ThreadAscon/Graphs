from pathlib import Path

from common import *
from data import *

PRINT_AVERAGES = True
USE_OLD_AVERAGES = False

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

  return averagesDict

if __name__ == "__main__":
  print(getAverages())