#coin exchange minimum coins
coins=list(map(int,input("Enter coins:").split()))
amount=int(input("Enter amount:"))
coins.sort(reverse=True)
count=0
for coin in coins:
    used=amount//coin
    count+=used
    amount=amount%coin
    if used>0:
        print(coin,"Rupees:",used,"coins")
if amount==0:
    print("minimum counts:",count)
else:
    print("cannot for exact amount")