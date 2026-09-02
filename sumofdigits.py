#Sum of digits of a given number
n=int(input("Enter a number:"))
sum=0
copy=n
while n!=0:
    digit=n%10
    sum+=digit
    n//=10
print("Sum of Digits of",copy,"is",sum)
