""" TODO: Create a data structure to hold all files containing trial data to parse for
          each individual experiment.
"""
from pathlib import Path

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-observe")
RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-observe", "data")

THESIS_TP_OBSERVE_LOGS = {
  "No Encryption": {
    "20 dBm": [],
    "9 dBm": [],
    "0 dBm": []
  },
  "AES": {
    "20 dBm": [],
    "9 dBm": [],
    "0 dBm": []
  },
  "ASCON-128a": {
    "20 dBm": [],
    "9 dBm": [],
    "0 dBm": []
  },
  "ASCON-128": {
    "20 dBm": [],
    "9 dBm": [],
    "0 dBm": []
  },
}