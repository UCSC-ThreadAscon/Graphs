import json
import numpy as np
import matplotlib as mpl
#mpl.use('pgf')
import matplotlib.pyplot as plt

EXPORT_FOR_LATEX = False

algs = ["None", "AES", "AsconAead-128"]
powers = ["0dbm", "9dbm", "20dbm"]
colors = {"None":"grey", "AES":"orange", "AsconAead-128":"blue"}


#----------------------------------- rtt
rtt_data = {}
with open('RTT-results.json', 'r') as file:
    rtt_data = json.load(file)

bar_width = 0.25
fontsize = "x-large"
fig = plt.subplots() 



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
    plt.bar(bar_pos, rtt_mean[alg], color = colors[alg], width = bar_width, label = alg) 
    plt.errorbar(bar_pos, rtt_mean[alg], yerr=rtt_err[alg], fmt="o", color="black")
    for i in range(len(bar_pos)):
        bar_pos[i] += bar_width

plt.title("Round Trip Time", fontsize = fontsize)
plt.xlabel('TX Power (dBm)', fontsize = fontsize) 
plt.ylabel('RTT (ms)', fontsize = fontsize) 
plt.xticks([r + bar_width for r in range(3)], powers)

plt.legend()

if (EXPORT_FOR_LATEX):
    plt.savefig('rtt-plot-bar.pgf', format='pgf')
else:
    plt.show()

#----------------------------------- cpu
cpu_data = {}
with open('CPU-results.json', 'r') as file:
    cpu_data = json.load(file)

bar_width = 0.25
fontsize = "x-large"
fig = plt.subplots() 



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
    plt.bar(bar_pos, cpu_mean[alg], color = colors[alg], width = bar_width, label = alg) 
    plt.errorbar(bar_pos, cpu_mean[alg], yerr=cpu_err[alg], fmt="o", color="black")
    for i in range(len(bar_pos)):
        bar_pos[i] += bar_width

plt.title("CPU Time Spent on Working Threads", fontsize = fontsize)
plt.xlabel('TX Power (dBm)', fontsize = fontsize) 
plt.ylabel('Percent (%)', fontsize = fontsize) 
plt.xticks([r + bar_width for r in range(3)], powers)

plt.legend()

if (EXPORT_FOR_LATEX):
    plt.savefig('cpu-plot-bar.pgf', format='pgf')
else:
    plt.show()


