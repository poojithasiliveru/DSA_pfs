#pancake sort/flip sort

def flip(arr,k):
    i=0
    j=k-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
def pancakesort(arr):
    for size in range(len(arr),1,-1):
        max_index=0
        for i in range(1,size):
            if arr[i]>arr[max_index]:
                max_index=i
        flip(arr,max_index+1)
        flip(arr,size)
    return arr
arr=list(map(int,input("Enter elements:").split()))
print("sorted array:",pancakesort(arr))