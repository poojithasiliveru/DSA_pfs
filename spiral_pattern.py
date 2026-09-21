#print sprial pattern
n=int(input("Enter n value: "))
num=1
matrix=[[0]*n for _ in range(n)]
left=0
right=n-1
top=0
bottom=n-1
while top<=bottom and left<=right:
    #left to right at top
    for i in range(left,right+1):
        matrix[top][i]=num
        num+=1
    top+=1
    #top to bottom at right
    for i in range(top,bottom+1):
        matrix[i][right]=num
        num+=1
    right-=1
    #right to left at bottom
    for i in range(right,left-1,-1):
        matrix[bottom][i]=num
        num+=1
    bottom-=1
    #bottom to top at left
    for i in range(bottom,top-1,-1):
        matrix[i][left]=num
        num+=1
    left+=1
for row in matrix:
    for value in row:
        print(f"{value:2d}",end=' ')
    print()
