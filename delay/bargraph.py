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

  for cipher, delaysDict in toDisplay.items():

    delaysMs = [(usToMs(delay) if delay != None else 0) for delay in delaysDict.values()]
    print(stds[cipher].values())

    stdsMs = [usToMs(std) for std in stds[cipher].values()]

    offset = width * multiplier
    rects = axis.bar(xAxisValues + offset, delaysMs, width, label=cipher,
                     color=cipherColors[cipher])

    if SHOW_BAR_LABELS:
      axis.bar_label(rects, padding=3, fontsize=FONT_SIZE)

    multiplier += 1

  axis.set_ylabel('Delay (ms)', fontsize=FONT_SIZE)
  axis.set_title(f'Average Delay', fontsize=FONT_SIZE)

  xWidthOffset = 0.30
  axis.set_xticks(xAxisValues + xWidthOffset, TX_POWERS_LABELS.values(),
                  fontsize=FONT_SIZE)

  # y_min = 19
  # y_lim = 23
  y_lim = 26
  y_min = 10

  tick_step = abs(y_lim - y_min) / 10
  ticks = np.arange(0, y_lim, tick_step)
  # ticks = np.append(ticks, [y_lim])

  axis.set_yticks(ticks)

  axis.tick_params(axis='y', labelsize=FONT_SIZE)
  axis.tick_params(axis='x', labelsize=FONT_SIZE)

  axis.legend(loc='best', ncols=2, fontsize=FONT_SIZE)
  axis.set_ylim(y_min, y_lim)

  axis.set_xlabel('TX Power (dBm)', fontsize=FONT_SIZE)

  if RENDER_PGF:
    plt.savefig(os.path.join(THESIS_FIGURES_PATH, 'delay-bar-graph.pgf'))
  return

if __name__ == "__main__":
  bargraph()

  if not RENDER_PGF:
    plt.show()