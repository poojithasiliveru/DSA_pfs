#back track n-queens
n=int(input("Enter n:"))
board=[["."]*n for _ in range(n)]
print(board)
def solve(row):
    if row==n:
        for line in board:
            print(" ".join(line))
        print()
        return
    for col in range(n):
        safe=True
        for i in range(row):
            if board[i][col]=='Q':
                safe=False
            if row-i==abs(col-board[i].index('Q')):
                safe=False
        if safe:
            board[row][col]='Q'
            solve(row+1)
            board[row][col]='.'
solve(0)

            