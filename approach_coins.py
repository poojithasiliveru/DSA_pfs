#coin exchange minimum coins denominations
coins=list(map(int,input("Enter coins:").split()))
amount=int(input("Enter amount:"))
coins.sort(reverse=True)
for coin in coins:
    count=amount//coin
    print(coin,"Rupees:",count,"coins")
    amount=amount%coin