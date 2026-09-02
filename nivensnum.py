#(number % sum of digits == 0)
n=int(input("Enter a number:"))
sum=0
temp=n
while n!=0:
    digit=n%10
    sum+=digit
    n//=10
if(temp%sum==0):
    print(temp,"is Niven's Number")
else:
    print(temp,"is Not a Niven's Number")
