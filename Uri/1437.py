# -*- coding: utf-8 -*-

'''
Turn Left!
URI 1437
https://www.urionlinejudge.com.br/judge/en/problems/view/1437
'''

def position(line):
  arr = ["N","L","S","O"]
  i = 0
  for c in line :
    if c == "E":
      i -= 1
    if c == "D":
      i +=1
  x = abs(i % 4)
  return arr[x]
  
while True:
  n = int(input())
  if n == 0:
    break
  i = input()
  print(position(i))