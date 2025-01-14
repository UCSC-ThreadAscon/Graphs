from pathlib import Path

LOCATION = "Santa-Cruz-Dec-2024"
LOCATION_STRING = "UCSC December 2024"

RESTARTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "delay", "restarts", "Santa-Cruz-Dec-2024")

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "delay")

THESIS_DELAY_AVERAGES = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Jan-2024", "delay-final-average-FIRST-1000-No Encrypt-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-AES-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-AES-9dbm.txt"),
    "0 dBm": None
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-ASCON-128a-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-ASCON-128-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  }
}

RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "delay", "data", "Santa-Cruz-Dec-2024")

THESIS_DELAY_LOGS = {
  "No Encryption": {
    "20 dBm": Path(RESULTS_PATH, "NoEncrypt-20dbm-trial-2", "delay-FTD-NoEncrypt-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "AES": {
    "20 dBm": Path(RESULTS_PATH, "AES-20dbm-trial-3", "delay-FTD-AES-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "AES-9dbm-trial-2", "delay-FTD-AES-9dbm.txt"),
    "0 dBm": None
  },
  "ASCON-128a": {
    "20 dBm": Path(RESULTS_PATH, "LibAscon-128a-20dbm-trial-2", "delay-FTD-LibAscon-128a-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128": {
    "20 dBm": Path(RESULTS_PATH, "LibAscon-128-20dbm-trial-2", "delay-FTD-LibAscon-128-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  }
}