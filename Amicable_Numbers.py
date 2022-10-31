
n=int(input())
m=int(input())
c=0
s=0
for i in range(1,(n//2)+1):
    if n%i==0:   
     c+=i
for j in range(1,(m//2)+1):
    if m%j==0:   
     s+=j
if (s==n and c==m):
        print("Amicable")
else:
        print("Not Amicable")
                   
