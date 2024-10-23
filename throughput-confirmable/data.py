from pathlib import Path

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-confirmable")
RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-confirmable", "data")

"""These files hold the Delay averages for the experiments I ran at home.
"""
THESIS_DELAY_AVERAGES = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-No Encrypt-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-AES-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-ASCON-128a-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128": {
    "20 dBm": None,
    "9 dBm": None,
    "0 dBm": None
  }
}

THESIS_DELAY_LOGS = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "data", "NoEncrypt-20dbm-trial-1", "tp-con-FTD-NoEncrypt-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "data", "AES-20dbm-trial-1", "tp-con-FTD-AES-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128a-20dbm-trial-1", "tp-con-LibAscon-128a-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128": {
    "20 dBm": None,
    "9 dBm": None,
    "0 dBm": None
  }
}