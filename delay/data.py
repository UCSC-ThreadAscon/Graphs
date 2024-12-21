from pathlib import Path

LOCATION = "Santa-Cruz-Dec-2024"
LOCATION_STRING = "UCSC December 2024"

RESTARTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "delay", "restarts", "Santa-Cruz-Dec-2024")

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "delay")

THESIS_DELAY_AVERAGES = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-No Encrypt-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-No Encrypt-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-No Encrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-AES-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-AES-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-ASCON-128a-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-ASCON-128a-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-ASCON-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-ASCON-128-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-ASCON-128-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "Santa-Cruz-Dec-2024", "delay-final-average-FIRST-1000-ASCON-128-0dbm.txt")
  }
}

RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "delay", "data", "Santa-Cruz-Dec-2024")

THESIS_DELAY_LOGS = {
  "No Encryption": {
    "20 dBm": Path(RESULTS_PATH, "NoEncrypt-20dbm-trial-1", "delay-FTD-NoEncrypt-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "NoEncrypt-9dbm-trial-1", "delay-FTD-NoEncrypt-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "NoEncrypt-0dbm-trial-1", "delay-FTD-NoEncrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(RESULTS_PATH, "AES-20dbm-trial-2", "delay-FTD-AES-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "AES-9dbm-trial-1", "delay-FTD-AES-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "AES-0dbm-trial-2", "delay-FTD-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(RESULTS_PATH, "LibAscon-128a-20dbm-trial-1", "delay-FTD-LibAscon-128a-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "LibAscon-128a-9dbm-trial-1", "delay-FTD-LibAscon-128a-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "LibAscon-128a-0dbm-trial-1", "delay-FTD-LibAscon-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(RESULTS_PATH, "LibAscon-128-20dbm-trial-1", "delay-FTD-LibAscon-128-20dbm.txt"),
    "9 dBm": Path(RESULTS_PATH, "LibAscon-128-9dbm-trial-1", "delay-FTD-LibAscon-128-9dbm.txt"),
    "0 dBm": Path(RESULTS_PATH, "LibAscon-128-0dbm-trial-1", "delay-FTD-LibAscon-128-0dbm.txt")
  }
}