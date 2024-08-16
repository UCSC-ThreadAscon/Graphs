from common import *

def getPercentIncrease(delayCipher, delayPlaintext):
  if (delayCipher < delayPlaintext):
    raise Exception(f"Cannot Get Percent Increase: {delayCipher} us < {delayPlaintext} us.")

  usDiff = delayCipher - delayPlaintext
  ratioDiff = usDiff / delayPlaintext
  percentDiff = ratioDiff * 100
  return percentDiff

if __name__ == "__main__":
  print(f"Percentage increase is {getPercentIncrease(20.3931, 19.4283):.5f} %.")