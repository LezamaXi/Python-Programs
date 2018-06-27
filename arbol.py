'''
Make the search in inorder in python
This is and example of how to use yield
'''

def in_order(arbol):
	if arbol == None : 
		return
	yield from in_order(arbol[1])
	yield arbol[0]
	yield from in_order(arbol[2])

arbol = (6,(4,(3,None,None),(5,None,None)),(8,(7,None,None),(10,(9,None,None),(11,None,None))))

for x in in_order(arbol):
	print(x)