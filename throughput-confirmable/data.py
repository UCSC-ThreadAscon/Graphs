from pathlib import Path

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-confirmable")
RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-confirmable", "data")

"""These files hold the Delay averages for the experiments I ran at home.
"""
THESIS_DELAY_AVERAGES = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-No Encrypt-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-No Encrypt-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-No Encrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-AES-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-AES-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-ASCON-128a-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-ASCON-128a-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-ASCON-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-ASCON-128-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-ASCON-128-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "home", "delay-final-average-FIRST-1000-ASCON-128-0dbm.txt")
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