ready/report.pdf: doc/report.pdf
	mkdir -p ./ready
	cp doc/report.pdf ready/report.pdf

ready/main-cli-debug: src/main.py
	mkdir -p ./ready
	cp src/* ready/
	mv ready/main.py ready/main-cli-debug.py

ready/stud-unit-test-report-prev.json: coverage/stud-unit-test-report-prev.json
	mkdir -p ./ready
	cp coverage/stud-unit-test-report-prev.json ready/

ready/stud-unit-test-report.json: coverage/stud-unit-test-report.json
	mkdir -p ./ready
	cp coverage/stud-unit-test-report.json ready/