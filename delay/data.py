from pathlib import Path

RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "Experiments", "delay", "data")
BEFORE_RECURSE_RESULTS_PATH = Path(RESULTS_PATH, "Before-Recurse-Submodules")

"""These files hold the Delay averages that I will use in the Thesis Writeup.
"""
THESIS_DELAY_AVERAGES={
  "No Encryption": {
    "20 dBm": Path(RESULTS_PATH, "NoEncrypt-20dbm-trial-1", "delay-final-average-No Encrypt-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "NoEncrypt-9dbm-trial-1", "delay-final-average-No Encrypt-9dbm.txt"),
    "0 dBm": None
  },
  "AES": {
    "20 dBm": Path(RESULTS_PATH, "AES-20dbm-trial-1", "delay-final-average-AES-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "AES-9dbm-trial-1", "delay-final-average-AES-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "AES-0dbm-trial-2", "delay-final-average-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(RESULTS_PATH, "LibAscon-128a-20dbm-trial-3", "delay-final-average-ASCON-128a-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "LibAscon-128a-9dbm-trial-1", "delay-final-average-ASCON-128a-9dbm.txt"),
    "0 dBm": None
  },
  "ASCON-128": {
    "20 dBm": Path(RESULTS_PATH, "LibAscon-128-20dbm-trial-1", "delay-final-average-ASCON-128-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "LibAscon-128-9dbm-trial-1", "delay-final-average-ASCON-128-9dbm.txt"),
    "0 dBm": None
  }
}

"""These file hold the averages that I gathered in previous, older experiments.
"""
PREV_DELAY_AVERAGES={
  "No Encryption": {
    "20 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "NoEncrypt-20dbm-trial-1", "delay-final-average-No Encrypt-20dbm.txt"),
    "9 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "NoEncrypt-9dbm-trial-2", "delay-final-average-No Encrypt-9dbm.txt"),
    "0 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "NoEncrypt-0dbm-trial-1", "delay-final-average-No Encrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "AES-20dbm-trial-1", "delay-final-average-AES-20dbm.txt"),
    "9 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "AES-9dbm-trial-1", "delay-final-average-AES-9dbm.txt"),
    "0 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "AES-0dbm-trial-1", "delay-final-average-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "LibAscon-128a-20dbm-trial-2", "delay-final-average-ASCON-128a-20dbm.txt"),
    "9 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "LibAscon-128a-9dbm-trial-3", "delay-final-average-ASCON-128a-9dbm.txt"),
    "0 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "LibAscon-128a-0dbm-trial-1", "delay-final-average-ASCON-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "LibAscon-128-20dbm-trial-1", "delay-final-average-ASCON-128-20dbm.txt"),
    "9 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "LibAscon-128-9dbm-trial-2", "delay-final-average-ASCON-128-9dbm.txt"),
    "0 dBm": Path(BEFORE_RECURSE_RESULTS_PATH, "LibAscon-128-0dbm-trial-1", "delay-final-average-ASCON-128-0dbm.txt")
  }
}
