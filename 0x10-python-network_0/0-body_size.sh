#!/bin/bash
#Bash script that uses curl to send a GET request to a given URL
#and then prints the size of the body of the response in bytes.

curl -s "$1" | wc -c
