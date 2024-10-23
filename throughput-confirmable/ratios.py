from common import *
from get_data import *

"""Given the final average throughput between encryption vs. throughput with no encryption,
   this function calculates the % INCREASE in throughput when using encryption vs. no encryption,
   RELATIVE to no encryption.

   NOTE that if the value returned is negative, the throughput under encryption is LESS than
        no encryption. In this case, the value return should be considered as a % DECREASE
        in throughput.
"""
def getPercentIncrease(throughputCipher, throughputPlaintext):
  usDiff = throughputCipher - throughputPlaintext
  ratioDiff = usDiff / throughputPlaintext
  percentDiff = ratioDiff * 100
  return percentDiff

def getThroughputRatios():
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
  averages = getAverages()

  for algorithm in algorithms:
    for txPower in TX_POWERS:
      cipherAverage = averages[algorithm][txPower]
      plaintextAverage = averages["No Encryption"][txPower]

      if (cipherAverage != None) and (plaintextAverage != None):
        ratiosDict[algorithm][txPower] = getPercentIncrease(cipherAverage, plaintextAverage)
        print(f"{algorithm} % INCREASE relative to No Encryption @ {txPower}: {ratiosDict[algorithm][txPower]} %.")

  return ratiosDict

if __name__ == "__main__":
  print(getThroughputRatios())
