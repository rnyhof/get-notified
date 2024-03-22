#!/bin/ksh

typeset -a JSON

function cache {
  typeset -i i=0
  while read JSON[$((i+=1))];do;:;done < "${1}"
}

function j1 {
  echo ${JSON[*]} | jq -r "${1}"
}

function j2 {
  echo "${1}" | jq -r "${2}"
}

cache 'etms43srv.json'

for i in {0..$(j1 '.packages|length')} ; do
  P=$(j1 ".packages[$((i-1))]")
  j2 "${P}" '[.name,.version,.revision]|@tsv' | read PN PV PR
  echo "${PN} ${PV} ${PR}"
done

exit 0
