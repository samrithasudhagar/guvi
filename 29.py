n=int(input())
if n<60:
  print(n)
else:
  r=n%60
  t=n//60
print (t,end=" ")
print(r)
