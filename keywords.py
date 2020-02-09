#!/usr/bin/python3
#-*- coding:UTF-8 -*-

f = open('keywords.txt','r')
lines = f.readlines()
#print(lines)

for line in lines:
  if '武汉' in line:
    if '中国' in line:
      print(line)



