n=int(input())
a=n*n
b=str(a)
c=str(n)
if b.endswith(c):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")