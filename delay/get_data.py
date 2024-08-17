from pathlib import Path

from common import *

RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "Experiments", "delay", "data")

PRINT_AVERAGES = True

"""These paths for the files which hold the Final Average Delays for each experiment.
"""
DATA_FILEPATHS={
  "No Encryption": {
    "20 dBm": Path(RESULTS_PATH, "NoEncrypt-20dbm-trial-1", "delay-final-average-No Encrypt-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "NoEncrypt-9dbm-trial-2", "delay-final-average-No Encrypt-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "NoEncrypt-0dbm-trial-1", "delay-final-average-No Encrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(RESULTS_PATH, "AES-20dbm-trial-1", "delay-final-average-AES-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "AES-9dbm-trial-1", "delay-final-average-AES-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "AES-0dbm-trial-1", "delay-final-average-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(RESULTS_PATH, "LibAscon-128a-20dbm-trial-1", "delay-final-average-ASCON-128a-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "LibAscon-128a-9dbm-trial-2", "delay-final-average-ASCON-128a-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "LibAscon-128a-0dbm-trial-1", "delay-final-average-ASCON-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(RESULTS_PATH, "LibAscon-128-20dbm-trial-1", "delay-final-average-ASCON-128-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "LibAscon-128-9dbm-trial-1", "delay-final-average-ASCON-128-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "LibAscon-128-0dbm-trial-1", "delay-final-average-ASCON-128-0dbm.txt")
  }
}

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

  for cipher in DATA_FILEPATHS.keys():
    for txPower in DATA_FILEPATHS[cipher].keys():
      filepath = DATA_FILEPATHS[cipher][txPower]

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