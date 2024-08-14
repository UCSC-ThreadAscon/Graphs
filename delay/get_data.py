from pathlib import Path

CIPHERS = ["AES", "ASCON-128a", "ASCON-128", "No Encryption"]
TX_POWERS = ["0 dBm", "9 dBm", "20 dBm"]

RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "Experiments", "delay", "data")

"""These paths for the files which hold the Final Average Delays for each experiment.
"""
DATA_FILEPATHS={
  "AES": {
    "20 dBm": Path(RESULTS_PATH, "AES-20dbm-trial-1", "delay-final-average-AES-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "AES-9dbm-trial-1", "delay-final-average-AES-9dbm.txt"),
    "0 dBm": None
  },
  "No Encryption": {
    "20 dBm": Path(RESULTS_PATH, "NoEncrypt-20dbm-trial-1", "delay-final-average-NoEncrypt-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "NoEncrypt-9dbm-trial-1", "delay-final-average-NoEncrypt-9dbm.txt"),
    "0 dBm": None
  },
  "ASCON-128a": {
    "20 dBm": Path(RESULTS_PATH, "LibAscon-128a-20dbm-trial-1", "delay-final-average-ASCON-128a-20dbm.txt"),
    "9 dBm": "",
    "0 dBm": ""
  },
  "ASCON-128": {
    "20 dBm": Path(RESULTS_PATH, "LibAscon-128-20dbm-trial-1", "delay-final-average-ASCON-128-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  }
}

def getAverages():
  return

if __name__ == "__main__":
  for cipher in DATA_FILEPATHS.keys():
    for txPower in DATA_FILEPATHS[cipher].keys():
      print(DATA_FILEPATHS[cipher][txPower])