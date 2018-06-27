def distancia(x1, y1, x2, y2):
	dx= x1 - x2
	dy= y1 - y2
	return((dx*dx + dy*dy)**0.5)

x1, x2 = map(float, input().split())
x3, x4 = map(float, input().split())
x = distancia(x1, x2, x3, x4)
j= '%.4f' % x
print(str(j))




