import matplotlib.pyplot as plt
import numpy as np

from get_data import *

SHOW_BAR_LABELS = True

toDisplay = getAverages()
print(toDisplay)

def bargraph():
  xAxisValues = np.arange(len(TX_POWERS))
  width = 0.2
  multiplier = 0

  figure, axis = plt.subplots(layout='constrained')

  if RENDER_PGF:
    figure.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
    figure.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  for cipher, avgThroughputsDict in toDisplay.items():

    avgThroughputs = [
      (avgThroughput if avgThroughput != None else 0)
      for avgThroughput in avgThroughputsDict.values()
    ]
    offset = width * multiplier
    rects = axis.bar(xAxisValues + offset, avgThroughputs, width, label=cipher,
                  color=cipherColors[cipher])

    if SHOW_BAR_LABELS:
      axis.bar_label(rects, padding=3)

    multiplier += 1

  axis.set_ylabel('Throughput (bytes/second)')
  axis.set_title(f'Average Throughput (Confirmable)')

  xWidthOffset = 0.30
  axis.set_xticks(xAxisValues + xWidthOffset, TX_POWERS_LABELS.values())

  y_min = 88
  y_lim = 93

  num_ticks = abs(y_lim - y_min) / 12
  ticks = np.arange(0, y_lim, num_ticks)
  ticks = np.append(ticks, [y_lim])

  axis.set_yticks(ticks)
  axis.legend(loc='best', ncols=4)
  axis.set_ylim(y_min, y_lim)

  axis.set_xlabel('TX Power (dBm)')

  if RENDER_PGF:
    plt.savefig(os.path.join(THESIS_FIGURES_PATH, 'throughput-confirmable-bar-graph.pgf'))
  return

if __name__ == "__main__":
  bargraph()

  if not RENDER_PGF:
    plt.show()