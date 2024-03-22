#!/bin/ksh

typeset -a JSON

function cache {
  [ ${#} -eq 1 ] || return 1
  [ -f "${1}" ] || return 1

  typeset -i i=0
  while read JSON[$((i+=1))];do;:;done < "${1}"

  return 0
}

function j1 {
  [ ${#} -eq 1 ] && echo ${JSON[*]} | jq -r "${1}"
}

function j2 {
  [ ${#} -eq 2 ] && echo "${1}" | jq -r "${2}"
}

cache 'etms43srv.json' || exit 1

for i in {1..$(j1 '.packages|length')} ; do
  PKG=$(j1 ".packages[$((i-1))]")
  j2 "${PKG}" '[.name,.version]|@tsv' | read PKG_N PKG_V
  echo "cluster package: ${PKG_N}-${PKG_V}"
done

for i in {1..$(j1 '.instances|length')} ; do
  INS=$(j1 ".instances[$((i-1))]")

  for j in {1..$(j1 "${INS}" '.packages|length')} ; do
    PKG=$(j2 "${INS}" ".packages[$((j-1))]")
    j2 "${PKG}" '[.name,.version]|@tsv' | read PKG_N PKG_V
    [ -z "${PKG_V}" ] && PKG_V='1'
    echo "instance ${j} package: ${PKG_N}-${PKG_V}"
  done
done

exit 0
