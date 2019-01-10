n=int(input())
if n<60:
  print("0",end=" ")
  print(n)
else:
  r=n%60
  t=n//60
print (t,end=" ")
print(r)
