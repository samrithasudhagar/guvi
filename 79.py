n,m=map(int,input().split())
a=n*m
for i in range(1,1000):
	if (i*i)==a:
		flag=0
		break
	else:
		flag=1
if a==0:
	print("yes")
elif flag!=0:
	print("no")
elif flag==0:
	print("yes")
	#i
