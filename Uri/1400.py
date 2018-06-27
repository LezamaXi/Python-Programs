# -*- coding: utf-8 -*-

'''
Counting Game
URI Online Judge | 1400
https://www.urionlinejudge.com.br/judge/en/problems/view/1400
'''

def numberX( n, m, k ):
	repeat = 0
	x = 1
	z = 1
	j = 1
	
	while True :
		if x == n and z > 0 :
			x = n
			z = -1
			
		if x == 1 and z < 0:
			x = 1
			z = 1
		
		if x == m :
			if "7" in str(j) or j % 7 == 0 :
				repeat += 1
				if repeat == k:
					return j
		j += 1
		x += z
		
	return -1
		

while True :
	n,m,k = map( int, input().split())
	if n == m and m == k and k == 0 :
		break
	print(numberX( n, m, k ))