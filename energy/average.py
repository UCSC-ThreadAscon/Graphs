import sys
import csv
from common import *
from data import *

MA_WAKEUP_MINIMUM = 2
UA_WAKEUP_MINIMUM = MA_WAKEUP_MINIMUM * 1000

""" TODO: Print the first 1000 entries of the PPK2 file.
"""

def getAvgUa():
  return