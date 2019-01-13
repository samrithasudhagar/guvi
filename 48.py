n=int(input())
sum=0
l=list(map(int,input().split()))
for i in range(0,len(l)):
	sum=sum+l[i]
avg=sum//n
print(avg)
#i
