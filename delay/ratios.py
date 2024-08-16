from common import *

"""Given the final average delay between encryption vs. delay with no encryption,
   this functionc calculates the % INCREASE in delay when using encryption vs. no encryption.

   NOTE that if the value returned is negative, the delay under encryption is LESS than
        no encryption. In this case, the value return should be considered as a % DECREASE
        in delay.
"""
def getPercentIncrease(delayCipher, delayPlaintext):
  usDiff = delayCipher - delayPlaintext
  ratioDiff = usDiff / delayPlaintext
  percentDiff = ratioDiff * 100
  return percentDiff

if __name__ == "__main__":
  print(f"Percentage increase is {getPercentIncrease(20.3931, 19.4283):.5f} %.")