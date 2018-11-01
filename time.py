y= input()
t=y.split(':')
h=t[0]
m=t[1]
a=t[2]
b=a.split()
s=a[0]+a[1]
x=a[2]+a[3]

if x=="AM":
    if int(h)==12:
        h="00"
        print(h+":"+m+(":")+s)
    else:
        print(h+":"+m+(":")+s)
if x=="PM":
    h=int(int(h)+12)
    if h>24:
        h=h-24
    print(str(h)+":"+m+(":")+s)
