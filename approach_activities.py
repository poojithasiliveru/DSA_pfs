#Activities
n=int(input("Enter n number of activities:"))
start=list(map(int,input("Enter start time:").split()))
end=list(map(int,input("Enter ed time:").split()))
a=[]
for i in range(n):
    a.append((start[i], end[i]))
a.sort(key=lambda x:x[1])
print("Selected activities:")
lastend=0
for s,e in a:
    if s>=lastend:
        print(s,e)
        lastend=e
        
