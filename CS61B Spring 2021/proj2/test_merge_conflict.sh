#!/usr/bin/env bash
cd "D:\Study\Mooc\CS61B Spring 2021\proj2" || { echo "Failure"; exit 1; }
make
rm -rf .gitlet/
rm ./*.txt
alias gitlet='java gitlet.Main'

gitlet init

echo "Hello World!" > test1.txt
gitlet add "test1.txt"
echo "Hello me" > test2.txt
gitlet add "test2.txt"
gitlet commit "add test 1 and 2"

echo "foo" >> test1.txt
gitlet add "test1.txt"
gitlet commit "change test 1"

gitlet branch "this"

# test merge conflict
gitlet checkout "this"
echo "what" > test3.txt
gitlet add "test3.txt"
gitlet commit "add test3 in this branch"
gitlet checkout "master"
echo "what is the fuck" > test3.txt
gitlet add "test3.txt"
gitlet commit "add test3333 in this branch"
gitlet merge "this"

gitlet status




