import matplotlib

RENDER_PGF = True

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

CIPHERS = ["No Encryption", "AES", "ASCON-128a", "ASCON-128"]
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

initEmptyDict = lambda : { 
    "No Encryption": { "0 dBm": None, "9 dBm": None, "20 dBm": None},
    "AES": { "0 dBm": None, "9 dBm": None, "20 dBm": None },
    "ASCON-128a": { "0 dBm": None, "9 dBm": None, "20 dBm": None },
    "ASCON-128": { "0 dBm": None, "9 dBm": None, "20 dBm": None }
  }