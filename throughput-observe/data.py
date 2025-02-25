""" TODO: Create a data structure to hold all files containing trial data to parse for
          each individual experiment.
"""
from pathlib import Path

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-observe")
RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-observe", "data")

THESIS_TP_OBSERVE_AVERAGES = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "tp-observe-final-average-No Encryption-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "tp-observe-final-average-AES-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "tp-observe-final-average-ASCON-128a-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "tp-observe-final-average-ASCON-128-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  }
}

THESIS_TP_OBSERVE_LOGS = {
  "No Encryption": {
    "20 dBm": [
      Path(SCRIPTS_PATH, "data", "NoEncrypt-20dbm-trial-1", "tp-observe-BR-NoEncrypt-20dbm.txt")
    ],
    "9 dBm": [],
    "0 dBm": []
  },
  "AES": {
    "20 dBm": [
      Path(SCRIPTS_PATH, "data", "AES-20dbm-trial-3", "tp-observe-BR-AES-20dbm.txt")
    ],
    "9 dBm": [],
    "0 dBm": []
  },
  "ASCON-128a": {
    "20 dBm": [
      Path(SCRIPTS_PATH, "data", "LibAscon-128a-20dbm-trial-1", "tp-observe-BR-LibAscon-128a-20dbm.txt")
    ],
    "9 dBm": [],
    "0 dBm": []
  },
  "ASCON-128": {
    "20 dBm": [
      Path(SCRIPTS_PATH, "data", "LibAscon-128-20dbm-Partial-1", "tp-observe-BR-LibAscon-128-20dbm.txt"),
      Path(SCRIPTS_PATH, "data", "LibAscon-128-20dbm-Partial-2", "tp-observe-BR-LibAscon-128-20dbm.txt"),
      Path(SCRIPTS_PATH, "data", "LibAscon-128-20dbm-trial-1", "tp-observe-BR-LibAscon-128-20dbm.txt")
    ],
    "9 dBm": [],
    "0 dBm": []
  },
}