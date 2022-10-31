n,m=map(int,input().split())
d=2  #3
h=1 #
while True:
  if n%d==0 and m%d==0:
    n=n//d #4
    m=m//d #6
    h=h*d   #2
  else:
      d+=1  #3
  if n<d or m<d: 
      break
print(h)
    