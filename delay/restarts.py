from data import *
from average import findFirstLine, removeAnsi

DEBUG = True

# Stop looking for restarts after the 1000th trial has run.
TERMINAL_STRING = "Finished running 1000 trials for current experiment."

num_restarts_dict = {
  "No Encryption": {
    "20 dBm": 0,
    "9 dBm": 0,
    "0 dBm": 0
  },
  "AES": {
    "20 dBm": 0,
    "9 dBm": 0,
    "0 dBm": 0
  },
  "ASCON-128a": {
    "20 dBm": 0,
    "9 dBm": 0,
    "0 dBm": 0
  },
  "ASCON-128": {
    "20 dBm": 0,
    "9 dBm": 0,
    "0 dBm": 0
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
        num_restarts_dict[cipher][txPower] += 1
  return

def getAllNumRestarts():
  for filesDict in THESIS_DELAY_LOGS.values():
    for logFile in filesDict.values():
      getNumRestarts(logFile)
  return

if __name__ == "__main__":
  getAllNumRestarts()
  print(num_restarts_dict)