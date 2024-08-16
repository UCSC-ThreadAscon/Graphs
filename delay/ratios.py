from common import *
from get_data import *

"""Given the final average delay between encryption vs. delay with no encryption,
   this functionc calculates the % INCREASE in delay when using encryption vs. no encryption,
   RELATIVE to no encryption.

   NOTE that if the value returned is negative, the delay under encryption is LESS than
        no encryption. In this case, the value return should be considered as a % DECREASE
        in delay.
"""
def getPercentIncrease(delayCipher, delayPlaintext):
  usDiff = delayCipher - delayPlaintext
  ratioDiff = usDiff / delayPlaintext
  percentDiff = ratioDiff * 100
  return percentDiff

def getDelayRatios():
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
  print(getDelayRatios())
