from pathlib import Path

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "packet-loss-confirmable")
RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "packet-loss-confirmable", "data")

THESIS_PL_CON_AVERAGES = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-No Encrypt-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-No Encrypt-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-No Encrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-AES-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-AES-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-ASCON-128a-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-ASCON-128a-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-ASCON-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-ASCON-128-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-ASCON-128-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-con-final-average-ASCON-128-0dbm.txt")
  }
}

THESIS_PL_CON_LOGS = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "data", "NoEncrypt-20dbm-trial-1", "pl-con-FTD-NoEncrypt-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "data", "NoEncrypt-9dbm-trial-1", "pl-con-FTD-NoEncrypt-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "data", "NoEncrypt-0dbm-trial-1", "pl-con-FTD-NoEncrypt-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "data", "AES-20dbm-trial-1", "pl-con-FTD-AES-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "data", "AES-9dbm-trial-1", "pl-con-FTD-AES-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "data", "AES-0dbm-trial-1", "pl-con-FTD-AES-0dbm.txt")
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128a-20dbm-trial-1", "pl-con-FTD-LibAscon-128a-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128a-9dbm-trial-1", "pl-con-FTD-LibAscon-128a-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128a-0dbm-trial-1", "pl-con-FTD-LibAscon-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128-20dbm-trial-1", "pl-con-FTD-LibAscon-128-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128-9dbm-trial-1", "pl-con-FTD-LibAscon-128-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "data", "LibAscon-128-0dbm-trial-1", "pl-con-FTD-LibAscon-128-0dbm.txt")
  }
}