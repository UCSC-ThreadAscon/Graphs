import matplotlib.pyplot as plt
import numpy as np

from get_data import *

SHOW_BAR_LABELS = False

toDisplay, stds = getAverages()
print(toDisplay)

def bargraph():
  xAxisValues = np.arange(len(TX_POWERS))
  width = 0.2
  multiplier = 0

  figure, axis = plt.subplots(layout='constrained')

  # if RENDER_PGF:
  #   figure.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  #   figure.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  for cipher, averagesDict in toDisplay.items():

    averages = [
      (avgThroughput if avgThroughput != None else 0)
      for avgThroughput in averagesDict.values()
    ]
    print(stds[cipher].values())

    offset = width * multiplier
    rects = axis.bar(xAxisValues + offset, averages, width, label=cipher,
                     color=cipherColors[cipher], yerr=list(stds[cipher].values()))

    if SHOW_BAR_LABELS:
      axis.bar_label(rects, padding=3)

    multiplier += 1

  axis.set_ylabel('Throughput (bytes/second)')
  axis.set_title(f'Average Throughput (Observe)')

  xWidthOffset = 0.30
  axis.set_xticks(xAxisValues + xWidthOffset, TX_POWERS_LABELS.values())

  y_min = 0.9
  y_lim = 1.2

  num_ticks = abs(y_lim - y_min) / 12
  ticks = np.arange(0, y_lim, num_ticks)
  ticks = np.append(ticks, [y_lim])

  axis.set_yticks(ticks)
  axis.legend(loc='best', ncols=4)
  axis.set_ylim(y_min, y_lim)

  axis.set_xlabel('TX Power (dBm)')

  if RENDER_PGF:
    plt.savefig(os.path.join(THESIS_FIGURES_PATH, 'throughput-observe-bar-graph.pgf'))
  return

if __name__ == "__main__":
  bargraph()

  if not RENDER_PGF:
    plt.show()