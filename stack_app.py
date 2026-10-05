#web browser history using stacks
stack=[]
while True:
    print("\n 1.visit website:")
    print("2.Back")
    print("3.Forward")
    choice=int(input("Enter your choice:"))
    if choice==1:
        website=input("Enter website:")
        stack.append(website)
        with open("history.txt", "a") as file:
            file.write(website+"\n")
        print("Visited:",website)
    elif choice==2:
        if len(stack)==0:
            print("No Previous pages....")
        else:
            stack.pop()
            if len(stack)==0:
                print("No Previous pages...")
            else:
                print("Back to",stack[-1])
    elif choice==3:
        print("Browser History")
        if len(stack)==0:
            print("History Empty...")
        else:
            for website in stack:
                print(website)
    elif choice==4:
        print("Exit")
    else:
        print("Invalid input...")