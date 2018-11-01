def inc(b):
    y=True
    for i in range(0, len(b)//2):
        if int(b[i])==int(b[i+1])-1:
            y=False
        else:
            return True
    return y

def check(a,x):
    u=(len(a)//2)
    v=(len(a)-1)
    if (int(a[0])!=1 or int(a[v])!=1 or a[0:u]!=a[v:u:-1] or inc(a)):
        return ('no')
    else:
        return ('yes')

n=int(input())
for i in range(n):
    num=int(input())
    s=input().split()
    if num%2==0:
        print('no')
    else:
        print(check(s, num))