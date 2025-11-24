import os
import re
import json

algs = ["AES", "AsconAead128", "NoEncrypt"]
powers = ["0dbm", "9dbm", "20dbm"]
pattern = "[0-9.]+ bytes\/second, or"

tp_dict = {}

for alg in algs:
    for p in powers:
        test = "TP-CON-" + alg + "-" + p
        i = 1
        while (os.path.exists("Data/cse253-experiments/Throughput-Confirmable/" + test + "-trial-" + str(i+1))):
            i += 1
        if (i > 1):
            test = test + "-trial-" + str(i)


        print("reading: " + test)
        file_name = "Data/cse253-experiments/Throughput-Confirmable/" + test + "/ftd.txt"
        f = open(file_name, "r", encoding='utf-8')
        text = f.read()

        test = "TP-CON-" + alg + "-" + p # remove trial num for easier parsing results

        matches = re.findall(pattern, text)
        tp_dict[test] = []
        for m in matches:
            tp_dict[test].append(float(m[:18]))

tp_results = open("TP-results.json", "w")
json.dump(tp_dict, tp_results, indent=4)


