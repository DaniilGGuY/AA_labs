ready/report.pdf: report/report.pdf
	mkdir -p ./ready
	cp report/report.pdf ready/report.pdf

ready/app-cli-debug: src/main.py
	mkdir -p ./ready
	cp src/* ready/
	mv ready/main.py ready/app-cli-debug.py

ready/stud-unit-test-report-prev.json: coverage/stud-unit-test-report-prev.json
	mkdir -p ./ready
	cp coverage/stud-unit-test-report-prev.json ready/

ready/stud-unit-test-report.json: coverage/stud-unit-test-report.json
	mkdir -p ./ready
	cp coverage/stud-unit-test-report.json ready/