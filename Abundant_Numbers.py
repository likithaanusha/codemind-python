n=int(input())
c=0
for i in range(1,n):
    if n%i==0:
        c+=i
    else:
        c+=0
if(c>n):
    print("True")
else:
    print("False")
        
 