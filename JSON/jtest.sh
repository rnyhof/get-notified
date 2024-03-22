#!/bin/ksh

set -A JSON

function jread {
  typeset -i i=0

  while read JSON[$((i+=1))] ; do
   :
  done < "${1}"
}

function jcat {
  echo ${JSON[*]}
}

function jexe {
  echo ${JSON[*]} | jq "${1}"
}

jread etms43srv.json

jexe '.packages|length'
