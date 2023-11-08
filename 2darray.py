x = int(input("Enter x: "))
y = int(input("Enter y: "))

array_2d = [[0]*y for i in range(x)]

for i in range(x):
    for j in range(y):
         array_2d[i][j] = (i*j)


print(array_2d)



