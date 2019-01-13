n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
    max1=l[0]
for i in range(0,len(l)):
    if l[i]<max1:
        max1=l[i]
print(max1,end=" ")
for i in range(0,len(l)):
    min1=l[0]
for i in range(0,len(l)):
    if l[i]>min1:
        min1=l[i]
print(min1)
#i
