from pathlib import Path

CSV_PATHS = Path(Path.home(), "Desktop", "Repositories", "graphs", "throughput-observe", "csv")

THESIS_ENERGY_CSV = {
  "No Encryption": {
    "20 dBm": Path(CSV_PATHS, "NoEncrypt-20dbm-trial-1.csv"),
    "9 dBm": Path(CSV_PATHS, "NoEncrypt-9dbm-trial-1.csv"),
    "0 dBm": Path(CSV_PATHS, "NoEncrypt-0dbm-trial-1.csv")
  },
  "AES": {
    "20 dBm": Path(CSV_PATHS, "AES-20dbm-trial-1.csv"),
    "9 dBm": Path(CSV_PATHS, "AES-9dbm-trial-1.csv"),
    "0 dBm": Path(CSV_PATHS, "AES-0dbm-trial-1.csv")
  },
  "ASCON-128a": {
    "20 dBm": Path(CSV_PATHS, "LibAscon-128a-20dbm-trial-1.csv"),
    "9 dBm": Path(CSV_PATHS, "LibAscon-128a-9dbm-trial-1.csv"),
    "0 dBm": Path(CSV_PATHS, "LibAscon-128a-0dbm-trial-1.csv")
  },
  "ASCON-128": {
    "20 dBm": Path(CSV_PATHS, "LibAscon-128-20dbm-trial-2.csv"),
    "9 dBm": Path(CSV_PATHS, "LibAscon-128-9dbm-trial-1.csv"),
    "0 dBm": Path(CSV_PATHS, "LibAscon-128-0dbm-trial-1.csv")
  }
}