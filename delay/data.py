from pathlib import Path

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "delay")
RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "delay", "data")
BEFORE_RECURSE_RESULTS_PATH = Path(RESULTS_PATH, "Before-Recurse-Submodules")

"""These files hold the Delay averages that I will use in the Thesis Writeup.
"""
THESIS_DELAY_AVERAGES = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-No Encrypt-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-No Encrypt-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-No Encrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-AES-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-AES-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-ASCON-128a-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-ASCON-128a-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-ASCON-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-ASCON-128-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-ASCON-128-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "delay-final-average-FIRST-1000-ASCON-128-0dbm.txt")
  }
}

THESIS_DELAY_AVERAGES_ALL = {
  "No Encryption": {
    "20 dBm": Path(RESULTS_PATH, "NoEncrypt-20dbm-trial-1", "delay-final-average-No Encrypt-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "NoEncrypt-9dbm-trial-1", "delay-final-average-No Encrypt-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "NoEncrypt-0dbm-trial-1", "delay-final-average-No Encrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(RESULTS_PATH, "AES-20dbm-trial-1", "delay-final-average-AES-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "AES-9dbm-trial-1", "delay-final-average-AES-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "AES-0dbm-trial-1", "delay-final-average-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(RESULTS_PATH, "ASCON-128a-20dbm-trial-1", "delay-final-average-ASCON-128a-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "ASCON-128a-9dbm-trial-1", "delay-final-average-ASCON-128a-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "ASCON-128a-0dbm-trial-1", "delay-final-average-ASCON-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(RESULTS_PATH, "ASCON-128-20dbm-trial-1", "delay-final-average-ASCON-128-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "ASCON-128-9dbm-trial-1", "delay-final-average-ASCON-128-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "ASCON-128-0dbm-trial-1", "delay-final-average-ASCON-128-0dbm.txt")
  }
}

THESIS_DELAY_LOGS = {
  "No Encryption": {
    "20 dBm": Path(RESULTS_PATH, "NoEncrypt-20dbm-trial-1", "delay-client-NoEncrypt-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "NoEncrypt-9dbm-trial-1", "delay-client-NoEncrypt-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "NoEncrypt-0dbm-trial-1", "delay-client-NoEncrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(RESULTS_PATH, "AES-20dbm-trial-1", "delay-client-AES-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "AES-9dbm-trial-1", "delay-client-AES-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "AES-0dbm-trial-1", "delay-client-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(RESULTS_PATH, "ASCON-128a-20dbm-trial-1", "delay-client-LibAscon-128a-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "ASCON-128a-9dbm-trial-1", "delay-client-LibAscon-128a-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "ASCON-128a-0dbm-trial-1", "delay-client-LibAscon-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(RESULTS_PATH, "ASCON-128-20dbm-trial-1", "delay-client-LibAscon-128-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "ASCON-128-9dbm-trial-1", "delay-client-LibAscon-128-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "ASCON-128-0dbm-trial-1", "delay-client-LibAscon-128-0dbm.txt")
  }
}