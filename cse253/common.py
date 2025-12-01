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

THESIS_FIGURES_PATH = '/Users/simeon/Desktop/Repositories/cse253-final-report/images/pgfs'
THESIS_PAPER_WIDTH_IN = 5.75113
THESIS_PAPER_HEIGHT_IN = 8.12659