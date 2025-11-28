import json
import matplotlib as mpl
import numpy as np
#mpl.use('pgf')
import matplotlib.pyplot as plt

EXPORT_FOR_LATEX = False
FONT_SIZE = 'xx-large'

algs = ["NoEncrypt", "AES", " Ascon-AEAD128"]
powers = ["0 dBm", "9 dBm", "20 dBm"]
lineType = {
  "NoEncrypt": 'o--', 
  "AES": 'o:',
  "Ascon-AEAD128": 'o-.'
}
colors = {"NoEncrypt":"mediumaquamarine", "AES":"deepskyblue", " Ascon-AEAD128":"plum"}

def translate(alg): # labels are different for tp, show the same way as rtt/cpu on plot
    if (alg == "NoEncrypt"):
        return "None"
    elif(alg == " Ascon-AEAD128"):
        return "Ascon-AEAD128"
    else:
        return alg

#----------------------------------- bar

tp_data = {}
with open('TP-results.json', 'r') as file:
    tp_data = json.load(file)

bar_width = 0.25
fontsize = "xx-large"
fig, axis = plt.subplots() 

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

print(tp_err)

bar_pos = [0.0, 1.0, 2.0]
for alg in algs:
  print(tp_err[alg])
  axis.bar(bar_pos, tp_mean[alg], color = colors[alg], width = bar_width, label = translate(alg)) 
  axis.errorbar(bar_pos, tp_mean[alg], yerr=tp_err[alg], fmt="o", color="black")
  for i in range(len(bar_pos)):
      bar_pos[i] += bar_width

axis.set_title("Average Throughput (Confirmable)", fontsize = FONT_SIZE)
axis.set_xlabel('TX Power (dBm)', fontsize = FONT_SIZE) 
axis.set_ylabel('Throughput (bytes/second)', fontsize = FONT_SIZE) 
axis.set_xticks([r + bar_width for r in range(3)], powers)

y_min = 40
y_lim = 135

tick_step = abs(y_lim - y_min) / 13
ticks = np.arange(0, y_lim, tick_step)

axis.set_yticks(ticks)

axis.legend(loc='best', ncols=3, fontsize=FONT_SIZE)

axis.tick_params(axis='y', labelsize=FONT_SIZE)
axis.tick_params(axis='x', labelsize=FONT_SIZE)

plt.tight_layout()

if (EXPORT_FOR_LATEX):
    axis.savefig('tp-plot-line.pgf', format='pgf')
else:
    plt.show()

#----------------------------------- line


fig, axis = plt.subplots() 
x_points = [0.0, 9.0, 20.0]
for alg in algs:
  print(alg)
  if (alg != "NoEncrypt"):
    inc = []
    for i in range(len(tp_mean["NoEncrypt"])):
      inc.append( ((tp_mean[alg][i] - tp_mean["NoEncrypt"][i]) / tp_mean["NoEncrypt"][i]) * 100 )
    axis.plot(x_points, inc, lineType[alg.replace(" ", "")], color = colors[alg], label = alg)

axis.set_title("Throughput Increase Relative To No Encryption", fontsize = FONT_SIZE)
axis.set_xlabel('TX Power (dBm)', fontsize = FONT_SIZE) 
axis.set_ylabel('Percentage %', fontsize = FONT_SIZE) 

axis.set_xticks([0, 9, 20], powers)

y_interval = 1
y_lim = 5
y_min = -10

y_ticks = np.arange(y_min, y_lim, y_interval)
y_ticks = np.append(y_ticks, [y_lim])
axis.set_yticks(y_ticks)

axis.tick_params(axis='y', labelsize=FONT_SIZE)
axis.tick_params(axis='x', labelsize=FONT_SIZE)

axis.legend(loc='best', ncols=3, fontsize=FONT_SIZE)

plt.axhline(linestyle='dotted', lw=1, color='gainsboro')
plt.tight_layout()

if (EXPORT_FOR_LATEX):
    axis.savefig('tp-plot-line.pgf', format='pgf')
else:
    plt.show()
