#!/usr/bin/env bash

MYPATH=$1; DATA=$(grep -oaRE '[A-Z2-7]{32}' ${MYPATH} 2> /dev/null | sort -u | grep -vE 'ABC|\:(.)\1{3}'); SECRET=$(echo "$DATA" | cut -d: -f 2); echo -e "Possible TOTP shared secrets found in:"; COUNTER=1; echo "$DATA" | cut -d: -f 1 | while read line; do echo -e -n "$line: "; echo -e "$(sed -n ${COUNTER}p <<< \"${SECRET}\" | sed 's/"//g')"; ((COUNTER++)); done
