#Manipulations on Arrays & Strings
#count the occurances in an array
'''
arr=input("Enter fruits:").split()
key=input("Enter key:")
count=0
for i in arr:
    if i==key:
        count+=1
print(count)
'''

#write a code to reverse a string
'''
s=input("Enter string:")
rev=""
for i in s:
    rev=i+rev
print(rev)
'''

#count the charater occurence in the string
'''
s=input("Enter string:")
c=input("Enter character:")
count=0
for i in s:
    if i==c:
        count+=1
print(count)
'''
#find character frequency
'''
s=input("Enter string:")
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
'''

#largest string length in the group of strings
'''
words=input("Enter elements:").split()
large=words[0]
for word in words:
    if len(word)>len(large):
        large=word
print("Largest is:",large)
'''
