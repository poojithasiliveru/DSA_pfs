#maze path
n=int(input("Enter n:"))
maze=[]
for i in range(n):
    maze.append(list(map(int,input().split())))
    def solve(row,col,path):
        if row==n-1 and col==n-1:
            print(path)
            return
        if row>=n or col>=n or maze[row][col]==0:
            return
        maze[row][col]==0
        solve(row+1,col,path+'D')
        solve(row,col+1,path+'R')
        maze[row][col]=1
solve(0,0,'')