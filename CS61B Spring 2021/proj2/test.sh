#!/usr/bin/env bash
cd "D:\Study\Mooc\CS61B Spring 2021\proj2" || { echo "Failure"; exit 1; }
make
rm -rf .gitlet/
alias gitlet='java gitlet.Main'

gitlet init

echo "Hello World!" > test1.txt
gitlet add "test1.txt"
echo "Hello me" > test2.txt
gitlet add "test2.txt"
gitlet commit "add text 1 and 2"

echo "foo" >> test1.txt
gitlet add "test1.txt"
gitlet commit "change text 1"

gitlet branch "this"

# test fast-forwarded
gitlet checkout "this"
echo "what" > text3.txt
gitlet add "text3.txt"
echo "foo" >> text1.txt
#gitlet commit "add text3 in this branch"
#gitlet add "text1.txt"
#gitlet commit "change text1 in this branch"

gitlet status







