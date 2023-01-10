#!/usr/bin/env bash
cd "D:\Study\Mooc\CS61B Spring 2021\proj2" || { echo "Failure"; exit 1; }
make
rm -rf .gitlet/
alias gitlet='java gitlet.Main'

gitlet init
echo "Hello World!" > test1.txt




