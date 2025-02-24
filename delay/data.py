from pathlib import Path

LOCATION = "Santa-Cruz-Jan-2025"
LOCATION_STRING = "UCSC January 2025"

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "delay")
RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "delay", "data")
RESTARTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "delay", "restarts")

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