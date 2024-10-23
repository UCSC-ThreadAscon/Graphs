from pathlib import Path

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-confirmable")
RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-confirmable", "data")

"""These files hold the Delay averages for the experiments I ran at home.
"""
THESIS_DELAY_AVERAGES = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-No Encrypt-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-No Encrypt-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-No Encrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-AES-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-AES-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-ASCON-128a-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-ASCON-128a-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-ASCON-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-ASCON-128-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-ASCON-128-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "tp-con-final-average-ASCON-128-0dbm.txt")
  }
}

THESIS_DELAY_LOGS = {
  "No Encryption": {
    "20 dBm": None,
    "9 dBm": None,
    "0 dBm": None
  },
  "AES": {
    "20 dBm": None,
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128a": {
    "20 dBm": None,
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128": {
    "20 dBm": None,
    "9 dBm": None,
    "0 dBm": None
  }
}