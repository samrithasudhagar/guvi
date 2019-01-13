s=input()
for i in s:
	if i.isalnum()==True:
		flag=0
		break
	else:
		flag=1
if flag==0:
	print("Yes")
else:
	print("No")
#i
