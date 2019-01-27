n,m=map(int,input().split())
a=n*m
for i in range(1,1000):
	if (i*i)==a:
		print("yes")
		flag=0
		break
	else:
		flag=1
if flag!=0:
	print("no")
  #i
