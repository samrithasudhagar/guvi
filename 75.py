s=input()
k=list(s)
for i in range(0,len(k)):
    if i==int(len(k)/2):
        k[i]="*"
        if len(k)%2==0:
            k[i-1]="*"
print("".join(k))
