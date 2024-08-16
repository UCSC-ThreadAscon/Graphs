import matplotlib.pyplot as plt
import numpy as np

from common import *
from ratios import *

RATIOS = getDelayRatios()

def linegraph():
  aes = RATIOS['AES'].values()
  ascon128 = RATIOS["ASCON-128"].values()
  ascon128a = RATIOS["ASCON-128a"].values()

  y_interval = 0.5
  y_lim = 7
  y_min = -2

  fig, ax = plt.subplots()

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  aes_lines = plt.plot(TX_POWERS, aes, 'o--', color=cipherColors['AES'], label='AES')
  ascon128a_lines = plt.plot(TX_POWERS, ascon128a, 'o:', color=cipherColors['ASCON-128a'], label='ASCON-128a')
  ascon128a_lines = plt.plot(TX_POWERS, ascon128, 'o-.', color=cipherColors['ASCON-128'],label='ASCON-128')

  y_ticks = np.arange(y_min, y_lim, y_interval)
  y_ticks = np.append(y_ticks, [100])
  ax.set_yticks(y_ticks)
  ax.set_xticks(TX_POWERS)
  ax.set_ylim(y_min, y_lim)

  ax.legend(loc='best', ncols=3)
  ax.set_ylabel('Percentage (%)')
  ax.set_xlabel('TX Power (dBm)')
  ax.set_title('Delay Percentage (%) Increase Relative to No Encryption')

  plt.axhline(linestyle='dotted', lw=1, color='gainsboro')

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-ratio-throughput.pgf'))


if __name__ == "__main__":
  linegraph()
  plt.show()