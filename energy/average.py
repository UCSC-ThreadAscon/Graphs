from common import *
from energy import *

def getAvgMahAll(cipher, tx_power):
  sum = 0
  for location in LOCATIONS_ENERGY:
    sum += getAvgMah(prelimData[location][cipher][tx_power])
  return sum / len(LOCATIONS_ENERGY)

"""
  EQUATION TO CALCULATE RATIO
  ---------------------------
  mAh_aes => mAh of AES cipher for a given location
  mAh_ascon => mAh of ASCON-128/a for a given location

  [ 1 - (mAh_ascon / mAh_aes) ]    *    100
        |-------------------|
         % mAh_ascon is made
        up relative to mAh_aes

  |---------------------------|
    % gap between mAh_ascon
    and mAh_aes

  For the value shown above:
    if > 0%, then it shows that mAh_ascon is % SMALLER than No Encryption.
    if < 0%, then it shows that mAH_ascon is % BIGGER than No Encryption.
  
  However, we want to show mAh_ascon being smaller as a decrease,
  and mAh_ascon being bigger as an increase.

  So, when we multiply by -1, we get:
    if > 0%, then it shows that mAh_ascon is % BIGGER than AES.
    if < 0%, then it shows that mAH_ascon is % AES than AES.

  The format of the ratios array:
  
    [   ratio @ 0 dBm,  ratio @ 9 dBm,  ratio @ 20dBm   ]
"""
def getMahRatios(location, cipher):
  ratios = []
  for tx in TX_POWERS:
    value_cipher = getAvgMah(finalDataMa[location][cipher][tx])
    value_aes = getAvgMah(finalDataMa[location]["noencrypt"][tx])

    ratio = 1 - (value_cipher / value_aes)
    ratio *= 100
    ratio *= -1

    ratios.append(ratio)
  return ratios