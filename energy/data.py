from pathlib import Path

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "energy")
CSV_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "energy", "csv")

AVERAGES_TEXT_FILE = Path(SCRIPTS_PATH, "final-averages.txt")

THESIS_ENERGY_CSV = {
  "No Encryption": {
    "20 dBm": Path(CSV_PATH, "NoEncrypt-20dbm-trial-1.csv"),
    "9 dBm": Path(CSV_PATH, "NoEncrypt-9dbm-trial-1.csv"),
    "0 dBm": Path(CSV_PATH, "NoEncrypt-0dbm-trial-1.csv")
  },
  "AES": {
    "20 dBm": Path(CSV_PATH, "AES-20dbm-trial-1.csv"),
    "9 dBm": Path(CSV_PATH, "AES-9dbm-trial-1.csv"),
    "0 dBm": Path(CSV_PATH, "AES-0dbm-trial-1.csv")
  },
  "ASCON-128a": {
    "20 dBm": Path(CSV_PATH, "LibAscon-128a-20dbm-trial-1.csv"),
    "9 dBm": Path(CSV_PATH, "LibAscon-128a-9dbm-trial-1.csv"),
    "0 dBm": Path(CSV_PATH, "LibAscon-128a-0dbm-trial-1.csv")
  },
  "ASCON-128": {
    "20 dBm": Path(CSV_PATH, "LibAscon-128-20dbm-trial-2.csv"),
    "9 dBm": Path(CSV_PATH, "LibAscon-128-9dbm-trial-1.csv"),
    "0 dBm": Path(CSV_PATH, "LibAscon-128-0dbm-trial-1.csv")
  }
}