#!/bin/bash
URL=$1
STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

if [ "$STATUS" -eq 200 ]; then
    echo "$URL is UP (status $STATUS)"
else
    echo "$URL is DOWN or having issues (status $STATUS)"
fi
