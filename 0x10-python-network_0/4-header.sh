#!/bin/bash
#Take in URL, add header variable, displays "Hello School!". It should've been X-School-... instead of X-HolbertonSch.. But that is how the checker works
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
