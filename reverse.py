
n=int(input("Enter a number:"))
temp=n
rev=0
while n!=0:
    d=n%10
    rev=(rev*10)+d
    n//=10
rev==temp
print("Reverse of a number:",rev)