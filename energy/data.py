from pathlib import Path

SCRIPTS_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "energy", "data", "cse253")
CSV_PATH = Path(Path.home(), "Desktop", "Repositories", "graphs", "energy", "csv", "cse253")

AVERAGES_TEXT_FILE = Path(Path.home(), "Desktop", "Repositories", "graphs", "energy", "final-averages.txt")

THESIS_ENERGY_CSV = {
  "No Encryption": {
    "20 dBm": Path(CSV_PATH, "NoEncrypt-20dbm-trial-1.csv"),
    "9 dBm": Path(CSV_PATH, "NoEncrypt-9dbm-trial-1.csv")
  },
  "AES": {
    "20 dBm": Path(CSV_PATH, "AES-20dbm-trial-1.csv"),
    "9 dBm": Path(CSV_PATH, "AES-9dbm-trial-1.csv")
  },
  "AsconAead128": {
    "20 dBm": Path(CSV_PATH, "AsconAead128-20dbm-trial-2.csv"),
    "9 dBm": Path(CSV_PATH, "AsconAead128-9dbm-trial-1.csv")
  },
}