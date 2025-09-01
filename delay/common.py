import os
import matplotlib

RENDER_PGF = True

FONT_SIZE = 'xx-large'

if RENDER_PGF:
  matplotlib.use("pgf")
  matplotlib.rcParams.update({
      "pgf.texsystem": "pdflatex",
      'font.family': 'serif',
      'text.usetex': True,
      'pgf.rcfonts': False,
  })

THESIS_FIGURES_PATH = '/Users/simeon/Desktop/Repositories/ThesisWriteup/images/pgfs'
THESIS_PAPER_WIDTH_IN = 5.75113
THESIS_PAPER_HEIGHT_IN = 8.12659

CIPHERS = ["AES", "ASCON-128a", "ASCON-128", "No Encryption"]
TX_POWERS = ["0 dBm", "9 dBm", "20 dBm"]

cipherColors = \
{
  'AES': 'deepskyblue',
  'ASCON-128a': 'plum',
  'ASCON-128': 'orange',
  'No Encryption': 'mediumaquamarine'
}

TX_POWERS_LABELS = \
{
  "0dbm": "0 dBm",
  "9dbm": "9 dBm",
  "20dbm": "20 dBm"
}

def usToMs(us):
  return us / 1000