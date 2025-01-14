from data import *
from average import findFirstLine, removeAnsi

DEBUG = True

# Stop looking for restarts after the 1000th trial has run.
TERMINAL_STRING = "Finished running 1000 trials for current experiment."

NUM_RESTARTS = {
  "No Encryption": {
    "0 dBm": 0,
    "9 dBm": 0,
    "20 dBm": 0
  },
  "AES": {
    "0 dBm": 0,
    "9 dBm": 0,
    "20 dBm": 0
  },
  "ASCON-128a": {
    "0 dBm": 0,
    "9 dBm": 0,
    "20 dBm": 0
  },
  "ASCON-128": {
    "0 dBm": 0,
    "9 dBm": 0,
    "20 dBm": 0
  }
}

def getIndepVars(logFile):
  line = findFirstLine("Cipher Suite:", logFile)
  words = line.split(" ")
  cipher = removeAnsi(words[5]).replace('\n', '')

  # If "No" gets parsed, it's actually supposed to be "No Encryption".
  # Since " " is used as a delimiter, the "Encryption" word will be missed
  # during the parsing process.
  #
  if cipher == "No":
    cipher = "No Encryption"

  line = findFirstLine("Max TX Power is:", logFile)
  words = line.split(" ")
  txPower = removeAnsi(words[7] + " " + words[8]).replace('\n', '')
  return cipher, txPower

def getNumRestarts(filepath):
  cipher, txPower = getIndepVars(filepath)
  if DEBUG:
    print(filepath)

  with open(filepath, 'r') as file:
    for line in file:
      if TERMINAL_STRING in line:
        if DEBUG:
          print(line)
        break
      elif "restart" in line:
        if DEBUG:
          print(line)
        NUM_RESTARTS[cipher][txPower] += 1
  return

def getAllNumRestarts():
  for filesDict in THESIS_PL_CON_LOGS.values():
    for logFile in filesDict.values():
      print(logFile)
      getNumRestarts(logFile)
  return

if __name__ == "__main__":
  getAllNumRestarts()
  print(NUM_RESTARTS)