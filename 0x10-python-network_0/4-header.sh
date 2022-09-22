#!/bin/bash
#Take in URL, add header variable, displays "Hello School!"
curl -sX GET -H "X-School-User-Id: 98" "$1"
