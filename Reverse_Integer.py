n=int(input())
r=0
i=0#3    32   
if n<0:     #-123
    n=-n    #
    i=1
    
while(n>0):  #123>0   12>0     1>0
    a=n%10   #3       2        1
    r=r*10+a  #0*10+3=3    30+2=32   320+1 321
    n=n//10   #123//10=12   12//10 =1
if i==0:   
   print(r)
else:
    print(-r)