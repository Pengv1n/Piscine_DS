#!/bin/sh

if [ $# -eq 1 ];
then
	tmp=$(echo $1 | sed 's/ /%20/g')
	curl "https://api.hh.ru/vacancies?text=${tmp}&page=0&per_page=20" | jq '.' > hh.json
else
	echo "Number arguments not equal one!"
fi
