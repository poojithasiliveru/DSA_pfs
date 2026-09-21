'''#print visited path
1 2 3                  o/p:1 2 3 6 9 8 7 4 5
4 5 6
7 8 9'''
    
n=int(input("Enter n value: "))
num=1
matrix=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(num)
        num+=1
    matrix.append(row)
print('Matrix: ')
for row in matrix:
    for v in row:
        print(v,end=' ')
    print()
left=0
right=n-1
top=0
bottom=n-1
print('Visited Path:')
while top<=bottom and left<=right:
    #left to right at top
    for i in range(left,right+1):
        print(matrix[top][i],end=' ')
        num+=1
    top+=1
    #top to bottom at right
    for i in range(top,bottom+1):
        print(matrix[i][right],end=' ')
        num+=1
    right-=1
    #right to left at bottom
    for i in range(right,left-1,-1):
        print(matrix[bottom][i],end=' ')
        num+=1
    bottom-=1
    #bottom to top at left
    for i in range(bottom,top-1,-1):
        print(matrix[i][left],end=' ')
        num+=1
    left+=1