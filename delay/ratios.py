from common import *

def getPercentIncrease(delayCipher, delayPlaintext):
  if (delayCipher < delayPlaintext):
    raise Exception(f"Cannot Get Percent Increase: {delayCipher} us < {delayPlaintext} us.")

  return

if __name__ == "__main__":
  print(getPercentIncrease(20.3931, 19.4283))