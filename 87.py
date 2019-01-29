n,m=map(int,input().split())
l=[]
k=[]
sum=1
for i in range(1,n+1):
	if n%i==0:
		l.append(i)
for i in range(1,m+1):
	if m%i==0:
		k.append(i)
for i in range(0,len(l)):
	for j in range(0,len(k)):
		if l[i]==k[j]:
			sum=sum*l[i]
			
print(sum)
