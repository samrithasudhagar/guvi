s=""
n=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(0,len(l)):
	s=s+str(l[i])+" "
print(s.strip())
#i
