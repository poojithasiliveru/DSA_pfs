#back tracking with binary numbers
n=int(input("Enter n:"))
def backtarck(s):
    if len(s)==n:
        print(s)
        return
    backtarck(s+'0')
    backtarck(s+'1')
backtarck('')