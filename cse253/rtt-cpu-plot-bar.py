import json
import numpy as np
import matplotlib as mpl
#mpl.use('pgf')
import matplotlib.pyplot as plt

from common import *

algs = ["None", "AES", "Ascon-AEAD128"]
powers = ["0 dBm", "9 dBm", "20 dBm"]
colors = {"None":"mediumaquamarine", "AES":"deepskyblue", "Ascon-AEAD128":"plum"}


#----------------------------------- rtt
rtt_data = {}
with open('RTT-results.json', 'r') as file:
    rtt_data = json.load(file)

bar_width = 0.25
fig, axis = plt.subplots(layout='constrained') 



rtt_mean = {}
rtt_err = {}
for alg in algs:
    rtt_mean[alg] = []
    rtt_err[alg] = []
    for p in powers:
        test = "RTT-" + alg + "-" + p
        mean = 0
        # average times, counting 10 backwards from last entry
        for i in range(len(rtt_data[test]) - 1, len(rtt_data[test]) - 11, -1):
            mean += rtt_data[test][i]
        mean = mean / 10
        mean = mean / 1000 # convert us to ms

        rtt_mean[alg].append(mean)

        # get standard deviation with np, convert units
        # unsure if this is the correct way to do it
        rtt_err[alg].append( np.std(rtt_data[test]) / 1000 ) 

bar_pos = [0.0, 1.0, 2.0]
for alg in algs:
    axis.bar(bar_pos, rtt_mean[alg], color = colors[alg], width = bar_width, label = alg) 
    axis.errorbar(bar_pos, rtt_mean[alg], yerr=rtt_err[alg], fmt="o", color="black")
    for i in range(len(bar_pos)):
        bar_pos[i] += bar_width

axis.set_title("Round Trip Time", fontsize = FONT_SIZE)
axis.set_xlabel('TX Power (dBm)', fontsize = FONT_SIZE) 
axis.set_ylabel('RTT (ms)', fontsize = FONT_SIZE) 
axis.set_xticks([r + bar_width for r in range(3)], powers)

y_min = 0
y_lim = 90

tick_step = abs(y_lim - y_min) / 13
y_ticks = np.arange(0, y_lim, tick_step)
y_ticks = np.append(y_ticks, [y_lim])
axis.set_yticks(y_ticks)

axis.legend(loc='best', ncols=3, fontsize=FONT_SIZE)

axis.tick_params(axis='y', labelsize=FONT_SIZE)
axis.tick_params(axis='x', labelsize=FONT_SIZE)
plt.tight_layout()

if (RENDER_PGF):
  axis.savefig(THESIS_FIGURES_PATH + '/rtt-plot-bar.pgf', format='pgf')
else:
  plt.show()

#----------------------------------- cpu
cpu_data = {}
with open('CPU-results.json', 'r') as file:
    cpu_data = json.load(file)

bar_width = 0.25
fig, axis = plt.subplots(layout='constrained') 

cpu_mean = {}
cpu_err = {}
for alg in algs:
    cpu_mean[alg] = []
    cpu_err[alg] = []
    for p in powers:
        test = "RTT-" + alg + "-" + p
        mean = 0
        # average times, counting 10 backwards from last entry
        for i in range(len(cpu_data[test]) - 1, len(cpu_data[test]) - 11, -1):
            mean += cpu_data[test][i]
        mean = mean / 10
        cpu_mean[alg].append(mean)

        # get standard deviation with np
        # unsure if this is the correct way to do it
        cpu_err[alg].append( np.std(cpu_data[test]) ) 

bar_pos = [0.0, 1.0, 2.0]
for alg in algs:
    print(rtt_err[alg])
    axis.bar(bar_pos, cpu_mean[alg], color = colors[alg], width = bar_width, label = alg) 
    axis.errorbar(bar_pos, cpu_mean[alg], yerr=cpu_err[alg], fmt="o", color="black")
    for i in range(len(bar_pos)):
        bar_pos[i] += bar_width

axis.set_title("CPU Time Spent on Working Threads", fontsize = FONT_SIZE)
axis.set_xlabel('TX Power (dBm)', fontsize = FONT_SIZE) 
axis.set_ylabel('Percent (%)', fontsize = FONT_SIZE) 
axis.set_xticks([r + bar_width for r in range(3)], powers)

y_min = 0
y_lim = 43

tick_step = abs(y_lim - y_min) / 13
ticks = np.arange(0, y_lim, tick_step)
axis.set_yticks(ticks)

axis.tick_params(axis='y', labelsize=FONT_SIZE)
axis.tick_params(axis='x', labelsize=FONT_SIZE)
plt.tight_layout()

axis.legend(loc='best', ncols=3, fontsize=FONT_SIZE)

if (RENDER_PGF):
  axis.savefig(THESIS_FIGURES_PATH + '/cpu-plot-bar.pgf', format='pgf')
else:
  plt.show()


