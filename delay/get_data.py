from pathlib import Path

CIPHERS = ["AES", "ASCON-128a", "ASCON-128", "No Encryption"]
TX_POWERS = ["0 dBm", "9 dBm", "20 dBm"]

RESULTS_PATH = Path(Path.home(), "Desktop", "Repositories", "Experiments", "delay", "data")

"""These files hold the Final Average Delays for each experiment.
"""
FILES={
  ""
}

def getAverages():
  return

if __name__ == "__main__":
  print(RESULTS_PATH)