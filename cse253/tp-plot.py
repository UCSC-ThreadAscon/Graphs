import json
import matplotlib as mpl
import numpy as np
#mpl.use('pgf')
import matplotlib.pyplot as plt

EXPORT_FOR_LATEX = False

algs = ["NoEncrypt", "AES", "AsconAead128"]
powers = ["0dbm", "9dbm", "20dbm"]
colors = {"NoEncrypt":"mediumaquamarine", "AES":"deepskyblue", "AsconAead128":"plum"}

def translate(alg): # labels are different for tp, show the same way as rtt/cpu on plot
    if (alg == "NoEncrypt"):
        return "None"
    elif(alg == "AsconAead128"):
        return "AsconAead-128"
    else:
        return alg

#----------------------------------- bar

tp_data = {}
with open('TP-results.json', 'r') as file:
    tp_data = json.load(file)

bar_width = 0.25
fontsize = "x-large"
fig = plt.subplots() 

tp_mean = {}
tp_err = {}
for alg in algs:
    tp_mean[alg] = []
    tp_err[alg] = []
    for p in powers:
        test = "TP-CON-" + alg + "-" + p
        mean = 0
        # average times, counting 10 backwards from last entry
        for i in range(len(tp_data[test]) - 1, len(tp_data[test]) - 11, -1):
            mean += tp_data[test][i]
        mean = mean / 10
        tp_mean[alg].append(mean)
        tp_err[alg].append(np.std(tp_data[test]))

bar_pos = [0.0, 1.0, 2.0]
for alg in algs:
    print(alg)
    print(tp_err[alg])
    plt.bar(bar_pos, tp_mean[alg], color = colors[alg], width = bar_width, label = translate(alg)) 
    plt.errorbar(bar_pos, tp_mean[alg], yerr=tp_err[alg], fmt="o", color="black")
    for i in range(len(bar_pos)):
        bar_pos[i] += bar_width

plt.title("Throughput", fontsize = fontsize)
plt.xlabel('TX Power (dBm)', fontsize = fontsize) 
plt.ylabel('bytes/second', fontsize = fontsize) 
plt.xticks([r + bar_width for r in range(3)], powers)

plt.legend()

if (EXPORT_FOR_LATEX):
    plt.savefig('tp-plot-line.pgf', format='pgf')
else:
    plt.show()

#----------------------------------- line


fontsize = "x-large"
fig = plt.subplots() 
x_points = [0.0, 9.0, 20.0]
for alg in algs:
    if (alg != "NoEncrypt"):
        inc = []
        for i in range(len(tp_mean["NoEncrypt"])):
            inc.append( ((tp_mean[alg][i] - tp_mean["NoEncrypt"][i]) / tp_mean["NoEncrypt"][i]) * 100 )
        plt.plot(x_points, inc, color = colors[alg], label = alg)

plt.title("Throughput Increase Relative To No Encryption", fontsize = fontsize)
plt.xlabel('TX Power (dBm)', fontsize = fontsize) 
plt.ylabel('Percentage %', fontsize = fontsize) 
plt.xticks([0, 9, 20], powers)

plt.legend()

if (EXPORT_FOR_LATEX):
    plt.savefig('tp-plot-line.pgf', format='pgf')
else:
    plt.show()
