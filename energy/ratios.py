from common import *
from get_data import *

"""Given the final average mAh between encryption vs. mAh with no encryption,
   this function calculates the % INCREASE in mAh when using encryption vs. no encryption,
   RELATIVE to no encryption.

   NOTE that if the value returned is negative, the mAh under encryption is LESS than
        no encryption. In this case, the value return should be considered as a % DECREASE
        in mAh.
"""
def getPercentIncrease(mahCipher, mahPlaintext):
  diff = mahCipher - mahPlaintext
  ratioDiff = diff / mahPlaintext
  percentDiff = ratioDiff * 100
  return percentDiff

def getMahRatios(averages):
  ratios = initEmptyDict()

  for algorithm in CIPHERS:
    for txPower in TX_POWERS:
      cipherAverage = averages[algorithm][txPower]
      plaintextAverage = averages["No Encryption"][txPower]

      if (cipherAverage != None) and (plaintextAverage != None):
        ratios[algorithm][txPower] = \
            getPercentIncrease(cipherAverage, plaintextAverage)

        print(f"{algorithm} % INCREASE relative to No Encryption @ " +
              f"{txPower}: {ratios[algorithm][txPower]} %.")

  return ratios

if __name__ == "__main__":
  mahDict, mahWakeupDict = getAverages()

  print("---- Deep Sleep Included ----")
  print(getMahRatios(mahDict))
  print()
  print("---- Wakeup Only ----")
  print(getMahRatios(mahWakeupDict))
