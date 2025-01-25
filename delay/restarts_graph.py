import matplotlib.pyplot as plt
import numpy as np

from common import *
from restarts import *

SHOW_BAR_LABELS = True

def bargraph():
  xAxisValues = np.arange(len(TX_POWERS))
  width = 0.2
  multiplier = 0

  figure, axis = plt.subplots(layout='constrained')

  if RENDER_PGF:
    figure.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
    figure.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  for cipher, restartsDict in NUM_RESTARTS.items():
    numRestarts = restartsDict.values()
    offset = width * multiplier
    rects = axis.bar(xAxisValues + offset, numRestarts, width, label=cipher,
                  color=cipherColors[cipher])

    if SHOW_BAR_LABELS:
      axis.bar_label(rects, padding=3)

    multiplier += 1

  axis.set_ylabel('Number of Restarts')
  axis.set_xlabel('TX Power (dBm)')
  axis.set_title(f'Number of Experimental Trial Restarts (Delay)')

  xWidthOffset = 0.30
  axis.set_xticks(xAxisValues + xWidthOffset, TX_POWERS_LABELS.values())

  y_min = 0
  y_lim = 10

  num_ticks = abs(y_lim - y_min) / 12
  ticks = np.arange(0, y_lim, num_ticks)
  ticks = np.append(ticks, [y_lim])

  axis.set_yticks(ticks)
  axis.legend(loc='best', ncols=4)
  axis.set_ylim(y_min, y_lim)

  if RENDER_PGF:
    plt.savefig(os.path.join(THESIS_FIGURES_PATH, 'delay-bar-graph.pgf'))
  return

def linegraph():
  aes = NUM_RESTARTS['AES'].values()
  ascon128 = NUM_RESTARTS["ASCON-128"].values()
  ascon128a = NUM_RESTARTS["ASCON-128a"].values()
  noEncrypt = ascon128a = NUM_RESTARTS["No Encryption"].values()

  y_interval = 11
  y_lim = 10
  y_min = -2

  fig, ax = plt.subplots()

  if RENDER_PGF:
    fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
    fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  plt.plot(TX_POWERS, aes, 'o--', color=cipherColors['AES'], label='AES')
  plt.plot(TX_POWERS, ascon128a, 'o:', color=cipherColors['ASCON-128a'], label='ASCON-128a')
  plt.plot(TX_POWERS, ascon128, 'o-.', color=cipherColors['ASCON-128'],label='ASCON-128')
  plt.plot(TX_POWERS, noEncrypt, 'o-.', color=cipherColors['No Encryption'],label='No Encryption')

  y_ticks = np.arange(y_min, y_lim, y_interval)
  y_ticks = np.append(y_ticks, [y_lim])
  ax.set_yticks(y_ticks)
  ax.set_xticks(TX_POWERS)
  ax.set_ylim(y_min, y_lim)

  ax.legend(loc='best', ncols=3)
  ax.set_ylabel('Number of Restarts')
  ax.set_xlabel('TX Power (dBm)')
  ax.set_title(f'Number of Experimental Trial Restarts (Delay)')

  plt.axhline(linestyle='dotted', lw=1, color='gainsboro')

  if RENDER_PGF:
    plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'delay-num-restarts.pgf'))
  return

if __name__ == "__main__":
  getAllNumRestarts()
  print(NUM_RESTARTS)

  bargraph()
  plt.show()