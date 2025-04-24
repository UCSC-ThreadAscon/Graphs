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