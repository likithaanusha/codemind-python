
n=int(input())
i=1  #2
a=0  #1
while i<=n:
    if n%i==0:
        a+=1
    i+=1
if a==2:
        print("prime")
else:
        print("not a prime")
