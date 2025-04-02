from common import *
from get_data import *

def getPercentIncrease(plPercentCipher, plPercentPlaintext):
  return plPercentCipher - plPercentPlaintext

def getPacketLossRatios():
  ratiosDict = {
    "AES": {
      "0 dBm": None,
      "9 dBm": None,
      "20 dBm": None
    },
    "ASCON-128a": {
      "0 dBm": None,
      "9 dBm": None,
      "20 dBm": None
    },
    "ASCON-128": {
      "0 dBm": None,
      "9 dBm": None,
      "20 dBm": None
    }
  }

  algorithms = ["AES", "ASCON-128a", "ASCON-128"]
  averages, _ = getAverages()

  for algorithm in algorithms:
    for txPower in TX_POWERS:
      cipherAverage = averages[algorithm][txPower]
      plaintextAverage = averages["No Encryption"][txPower]

      if (cipherAverage != None) and (plaintextAverage != None):
        ratiosDict[algorithm][txPower] = getPercentIncrease(cipherAverage, plaintextAverage)
        print(f"{algorithm} % INCREASE relative to No Encryption @ {txPower}: {ratiosDict[algorithm][txPower]} %.")

  return ratiosDict

if __name__ == "__main__":
  print(getPacketLossRatios())
