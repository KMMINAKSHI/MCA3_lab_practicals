X = [[0,1,2],[3 ,4,5],[8 ,7,6]]

Y = [[5,6,7],[8,9,3],[4,2,1]]


result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
	for j in range(len(X[0])):
		result[i][j] = X[i][j] + Y[i][j]
print("After Addition of Matrix x and Y Resultant matrix is:")
for e in result:
	print(e)
