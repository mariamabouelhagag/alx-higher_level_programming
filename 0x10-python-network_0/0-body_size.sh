#!/bin/bash
#Bash script that uses curl to send a GET request to a given URL
#and then prints the size of the body of the response in bytes.

if [ "$#" -ne 1 ]; then
	echo "Usage: $0 url"
	exit 1

fi
url=$1

content_length=$(curl -sI -X HEAD $url | awk '/Content-Length/{print $2}')
echo "Body size: $content_length bytes"
