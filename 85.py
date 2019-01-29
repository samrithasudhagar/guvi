a=input()
k=list(a)
s=""
l=""
for i in range(0,len(k)):
	if i%2==0:
		s=s+str(k[i])+""
	if i%2==1:
		l=l+str(k[i])+""
print(s.strip(),end=" ")
print(l.strip())
#i
