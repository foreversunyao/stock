#!/bin/bash
today=$(date -v-0d +"%Y%m%d")
yesterday=$(date -v-1d +"%Y%m%d")
echo $today $yesterday
/usr/local/bin/python stockinfo_collect.py $yesterday $today
if [ $? -eq 0 ]
then
	echo "success"
fi

