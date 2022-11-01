n=int(input())
a=list(str(n))
d=1
r=0
for i in a:
    c=int(i)
    b=pow(c,d)
    d+=1
    r+=b
if (r==n):
    print("True")
else:
    print("False")
        
   