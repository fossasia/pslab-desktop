#!/bin/bash

IFS=$'\n';
for dir in "./templates";#$(find ./ -type d -name "templates"); 
do
	for f in $(find $dir -type f -name \*.py); 
	do 
		if [[ $f =~ "__init__.py" ]];then
			echo $f; 
		fi
	done
done
