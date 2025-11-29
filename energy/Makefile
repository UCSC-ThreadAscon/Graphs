average:
	rm -r -f ./final-averages.txt
	date | tee final-averages.txt
	#
	# Need "-u" flag for Python to not buffer `stdout` output when
	# `stdout` is being piped to the `tee` command:
	#	https://stackoverflow.com/a/27534908/6621292
	#
	python3 -u ./average.py | tee -a final-averages.txt

get_data:
	python3 ./get_data.py

get_std:
	python3 ./get_std.py

bargraph:
	python3 ./bargraph.py

bargraph_wakeup:
	python3 ./bargraph_wakeup.py

ratios:
	python3 ./ratios.py

linegraph:
	python3 ./linegraph.py

linegraph_wakeup:
	python3 ./linegraph_wakeup.py

linegraph_std:
	python3 ./linegraph_std.py

linegraph_wakeup_std:
	python3 ./linegraph_wakeup_std.py