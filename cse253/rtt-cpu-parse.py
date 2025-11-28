import os
import re
import json

algs = ["AES", "Ascon-AEAD128", "None"]
powers = ["0dbm", "9dbm", "20dbm"]

rtt_dict = {}
rtt_pattern = "Average RTT Time microseconds:\nI\([0-9]+\) OPENTHREAD:\[N\] Platform------: [0-9]+ us"

cpu_dict = {}
cpu_use_dict = {}
cpu_patterns = {
    "ot_cli_main": "ot_cli_main    	[0-9]+",
    "IDLE": "IDLE           	[0-9]+",
    "tcpip": "tcpip          	[0-9]+",
    "sys_evt": "sys_evt        	[0-9]+",
    "esp_timer": "esp_timer      	[0-9]+",
    "Tmr Svc": "Tmr Svc        	[0-9]+"
}

for alg in algs:
    for p in powers:
        test = "RTT-" + alg + "-" + p
        i = 1
        while (os.path.exists("Data/cse253-experiments/RTT-CPU-Usage/" + test + "-trial-" + str(i+1))):
            i += 1
        if (i > 1):
            test = test + "-trial-" + str(i)


        print("reading: " + test)
        file_name = "Data/cse253-experiments/RTT-CPU-Usage/" + test + "/ftd.txt"
        f = open(file_name, "r", encoding='utf-8')
        text = f.read()

        test = "RTT-" + alg + "-" + p # remove trial num for easier parsing results

        matches = re.findall(rtt_pattern, text)
        rtt_dict[test] = []
        for m in matches:
            t = re.search("[0-9]+ us", m)
            rtt_dict[test].append(int(m[t.span()[0]:t.span()[1]-3]))

        cpu_dict[test] = {}
        for pat in cpu_patterns:
            matches = re.findall(cpu_patterns[pat], text)
            cpu_dict[test][pat] = []
            for m in matches:
                cpu_dict[test][pat].append(m[16:])

        for test in cpu_dict:
            cpu_use_dict[test] = []
            for i in range(len(cpu_dict[test]["ot_cli_main"]) - 1, len(cpu_dict[test]["ot_cli_main"]) - 11, -1):
                total_time = 0
                for pat in cpu_patterns:
                    total_time += int(cpu_dict[test][pat][i])
                use_time = int(cpu_dict[test]["ot_cli_main"][i]) + int(cpu_dict[test]["tcpip"][i])
                cpu_use_dict[test].insert(0, (use_time / total_time)*100)



rtt_results = open("RTT-results.json", "w")
json.dump(rtt_dict, rtt_results, indent=4)

cpu_results = open("CPU-results.json", "w")
json.dump(cpu_use_dict, cpu_results, indent=4)
#json.dump(cpu_dict, cpu_results, indent=4)

