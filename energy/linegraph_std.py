import matplotlib.pyplot as plt
import numpy as np
import os

from common import *
from ratios import *
from get_std import getStds

stdsDict, _ = getStds()
print(stdsDict)

def linegraph():
  aes = stdsDict['AES'].values()
  asconaead128 = stdsDict["AsconAead128"].values()

  y_interval = 0.25
  y_lim = 19
  y_min = 16

  fig, ax = plt.subplots()

  # if RENDER_PGF:
  #   fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  #   fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  plt.plot(TX_POWERS, aes, 'o--', color=cipherColors['AES'], label='AES')
  plt.plot(TX_POWERS, asconaead128, 'o:', color=cipherColors['AsconAead128'],
           label='AsconAead128')

  y_ticks = np.arange(y_min, y_lim, y_interval)
  y_ticks = np.append(y_ticks, [y_lim])
  ax.set_yticks(y_ticks)
  ax.set_xticks(TX_POWERS)
  ax.set_ylim(y_min, y_lim)

  ax.legend(loc='best', ncols=2, fontsize=FONT_SIZE)
  ax.set_ylabel('Standard Deviation (mAh)', fontsize=FONT_SIZE)
  ax.set_xlabel('TX Power (dBm)', fontsize=FONT_SIZE)
  ax.set_title(f'Standard Deviations (Deep Sleep)',
               fontsize=FONT_SIZE)

  ax.tick_params(axis='y', labelsize=FONT_SIZE)
  ax.tick_params(axis='x', labelsize=FONT_SIZE)

  plt.axhline(linestyle='dotted', lw=1, color='gainsboro')
  plt.tight_layout()

  if RENDER_PGF:
    plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'std-linegraph.pgf'))
  return

if __name__ == "__main__":
  linegraph()

  if not RENDER_PGF:
    plt.show()