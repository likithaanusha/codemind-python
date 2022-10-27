N=int(input())
Summ=0
mul=1
while(N>0):
    a=N%10
    Summ+=a
    mul=mul*a
    N=N//10
if (Summ==mul):
        print("Spy Number")
else:
        print("Not Spy Number")
