#!/bin/bash
# send a request to an URL with curl, and displays the size of the body of the response
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 url"
    exit 1
fi

url=$1
content_length=$(curl -sI -X HEAD $url | awk '/Content-Length/{print $2}')
echo "Body size: $content_length bytes"
