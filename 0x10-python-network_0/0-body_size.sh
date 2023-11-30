#!/usr/bin/env bash

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Get the size of the body of the response
size=$(curl -sLI $URL | grep Content-Length | awk '{print $2}')

if [[ -z $size ]]; then
  echo "Error: Unable to get size of response body"
  exit 1
fi

echo "Size of response body: $size bytes"
