n=int(input())
a=str(n)
b=list(a)
c=0
d=0
for i in b:
 if int(i)%2==0:
     c+=1
  
    
 elif int(i)%2!=0:
     d+=1
if len(b)==c:
    print("Even")
elif len(b)==d:   
    print("Odd")
else:
    print("Mixed")