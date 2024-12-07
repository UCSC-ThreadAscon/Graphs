from pathlib import Path

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-confirmable")
RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-confirmable", "data")

THESIS_TP_CON_AVERAGES = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "tp-con-final-average-No Encrypt-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "tp-con-final-average-AES-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "tp-con-final-average-ASCON-128a-20dbm.txt"),
    "9 dBm": None,
    "0 dBm": None
  },
  "ASCON-128": {
    "20 dBm": None,
    "9 dBm": None,
    "0 dBm": None
  }
}

THESIS_TP_CON_LOGS = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "data", "NoEncrypt-20dbm-trial-1", "tp-con-FTD-NoEncrypt-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "data", "NoEncrypt-9dbm-trial-1", "tp-con-FTD-NoEncrypt-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "data", "NoEncrypt-0dbm-trial-1", "tp-con-FTD-NoEncrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "data", "AES-20dbm-trial-3", "tp-con-FTD-AES-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "data", "AES-9dbm-trial-1", "tp-con-FTD-AES-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "data", "AES-0dbm-trial-1", "tp-con-FTD-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128a-20dbm-trial-1", "tp-con-FTD-LibAscon-128a-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128a-9dbm-trial-1", "tp-con-FTD-LibAscon-128a-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128a-0dbm-trial-1", "tp-con-FTD-LibAscon-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128-20dbm-trial-1", "tp-con-FTD-LibAscon-128-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128-9dbm-trial-1", "tp-con-FTD-LibAscon-128-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128-0dbm-trial-1", "tp-con-FTD-LibAscon-128-0dbm.txt")
  }
}