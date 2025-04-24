#!/bin/bash
while read p; do
	echo "$p"
	python3 match.py $p >> matchOutput.txt
done <matchInput.txt
