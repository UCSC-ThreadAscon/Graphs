import json
import matplotlib as mpl
#mpl.use('pgf')
import matplotlib.pyplot as plt

EXPORT_FOR_LATEX = False
FONT_SIZE = 'xx-large'

algs = ["None", "AES", "Ascon-AEAD128"]
powers = ["0 dBm", "9 dBm", "20 dBm"]
lineType = {
  "NoEncrypt": 'o--', 
  "AES": 'o:',
  "Ascon-AEAD128": 'o-.'
}
colors = {"None":"mediumaquamarine", "AES":"deepskyblue", "Ascon-AEAD128":"plum"}


#----------------------------------- rtt
rtt_data = {}
with open('RTT-results.json', 'r') as file:
    rtt_data = json.load(file)

fig, axis = plt.subplots(layout='constrained')

rtt_mean = {}
for alg in algs:
    rtt_mean[alg] = []
    for p in powers:
        test = "RTT-" + alg + "-" + p
        mean = 0
        # average times, counting 10 backwards from last entry
        for i in range(len(rtt_data[test]) - 1, len(rtt_data[test]) - 11, -1):
            mean += rtt_data[test][i]
        mean = mean / 10
        rtt_mean[alg].append(mean)

for alg in algs:
  if (alg != "None"):
    for i in range(3):
      rtt_mean[alg][i] = (rtt_mean[alg][i] - rtt_mean["None"][i]) / rtt_mean["None"][i]

x_points = [0, 9, 20]
for alg in algs:
  print(alg)
  if (alg != "None"):
    axis.plot(x_points, rtt_mean[alg], lineType[alg],
      color = colors[alg], label = alg) 

axis.set_title("RTT Increase Relative To No Encryption", fontsize = FONT_SIZE)
axis.set_xlabel('TX Power (dBm)', fontsize = FONT_SIZE) 
axis.set_ylabel('Percentage (%)', fontsize = FONT_SIZE) 
axis.set_xticks([1, 9, 20], powers)
plt.tight_layout()

axis.legend(loc='best', ncols=3, fontsize=FONT_SIZE)

if (EXPORT_FOR_LATEX):
    axis.savefig('rtt-plot-line.pgf', format='pgf')
else:
    plt.show()

#----------------------------------- cpu
cpu_data = {}
with open('CPU-results.json', 'r') as file:
    cpu_data = json.load(file)

fontsize = "x-large"
fig, axis = plt.subplots(layout='constrained') 



cpu_mean = {}
for alg in algs:
  cpu_mean[alg] = []
  for p in powers:
    test = "RTT-" + alg + "-" + p
    mean = 0
    # average times, counting 10 backwards from last entry
    for i in range(len(cpu_data[test]) - 1, len(cpu_data[test]) - 11, -1):
      mean += cpu_data[test][i]
    mean = mean / 10
    cpu_mean[alg].append(mean)

for alg in algs:
  if (alg != "None"):
    for i in range(3):
      rtt_mean[alg][i] = (rtt_mean[alg][i] - rtt_mean["None"][i]) / rtt_mean["None"][i]

x_points = [0, 9, 20]
for alg in algs:
  if (alg != "None"):
    axis.plot(x_points, rtt_mean[alg], lineType[alg.replace(" ", "")], 
      color = colors[alg], label = alg)

axis.set_title("CPU Time Increase Relative To No Encryption", fontsize = FONT_SIZE)
axis.set_xlabel('TX Power (dBm)', fontsize = FONT_SIZE) 
axis.set_ylabel('Percentage (%)', fontsize = FONT_SIZE) 
axis.set_xticks([0, 9, 20], powers)

axis.legend(loc='best', ncols=3, fontsize=FONT_SIZE)
plt.tight_layout()

if (EXPORT_FOR_LATEX):
    axis.savefig('cpu-plot-line.pgf', format='pgf')
else:
    plt.show()


