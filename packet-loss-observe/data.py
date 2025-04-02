from pathlib import Path

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "packet-loss-observe")
RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "packet-loss-observe", "data")

THESIS_PL_OBSERVE_AVERAGES = {
  "No Encryption": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-observe-final-average-No Encryption-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-observe-final-average-No Encryption-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-observe-final-average-No Encryption-0dbm.txt")
  },
  "AES": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-observe-final-average-AES-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-observe-final-average-AES-9dbm.txt"),
    "0 dBm": None
  },
  "ASCON-128a": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-observe-final-average-ASCON-128a-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-observe-final-average-ASCON-128a-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-observe-final-average-ASCON-128a-0dbm.txt")
  },
  "ASCON-128": {
    "20 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-observe-final-average-ASCON-128-20dbm.txt"),
    "9 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-observe-final-average-ASCON-128-9dbm.txt"),
    "0 dBm": Path(SCRIPTS_PATH, "final-averages", "pl-observe-final-average-ASCON-128-0dbm.txt")
  }
}

THESIS_PL_OBSERVE_LOGS = {
  "No Encryption": {
    "20 dBm": [
      Path(SCRIPTS_PATH, "data", "NoEncrypt-20dbm-Partial-1", "pl-observe-BR-NoEncrypt-20dbm.txt"),
      Path(SCRIPTS_PATH, "data", "NoEncrypt-20dbm-trial-1", "pl-observe-BR-NoEncrypt-20dbm.txt"),
    ],
    "9 dBm": [
      Path(SCRIPTS_PATH, "data", "NoEncrypt-9dbm-Partial-1", "pl-observe-BR-NoEncrypt-9dbm.txt"),
      Path(SCRIPTS_PATH, "data", "NoEncrypt-9dbm-trial-1", "pl-observe-BR-NoEncrypt-9dbm.txt")
    ],
    "0 dBm": [
      Path(SCRIPTS_PATH, "data", "NoEncrypt-0dbm-trial-1", "pl-observe-BR-NoEncrypt-0dbm.txt")
    ]
  },
  "AES": {
    "20 dBm": [
      Path(SCRIPTS_PATH, "data", "AES-20dbm-trial-1", "pl-observe-BR-AES-20dbm.txt")
    ],
    "9 dBm": [
      Path(SCRIPTS_PATH, "data", "AES-9dbm-trial-1", "pl-observe-BR-AES-9dbm.txt")
    ],
    "0 dBm": []
  },
  "ASCON-128a": {
    "20 dBm": [
      Path(SCRIPTS_PATH, "data", "LibAscon-128a-20dbm-trial-1", "pl-observe-BR-LibAscon-128a-20dbm.txt")
    ],
    "9 dBm": [
      Path(SCRIPTS_PATH, "data", "LibAscon-128a-9dbm-trial-1", "pl-observe-BR-LibAscon-128a-9dbm.txt")
    ],
    "0 dBm": [
      Path(SCRIPTS_PATH, "data", "LibAscon-128a-0dbm-trial-2", "pl-observe-BR-LibAscon-128a-0dbm.txt")
    ]
  },
  "ASCON-128": {
    "20 dBm": [
      Path(SCRIPTS_PATH, "data", "LibAscon-128-20dbm-trial-1", "pl-observe-BR-LibAscon-128-20dbm.txt")
    ],
    "9 dBm": [
      Path(SCRIPTS_PATH, "data", "LibAscon-128-9dbm-trial-1", "pl-observe-BR-LibAscon-128-9dbm.txt")
    ],
    "0 dBm": [
      Path(SCRIPTS_PATH, "data", "LibAscon-128-0dbm-trial-1", "pl-observe-BR-LibAscon-128-0dbm.txt")
    ]
  }
}