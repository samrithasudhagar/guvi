#i
a,d,n=map(int,input().split())
s=0
for i in range(1,n+1):
	s=s+a+(i-1)*d
print(s)
