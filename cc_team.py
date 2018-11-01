num=int(input())
for i  in range(num):
    a=[]
    b=[]
    n,m=input().split()

    for j in range(int(m)):
        x,y= input().split()
        a.append(x)
        b.append(y)

    if int(n)%2==1:
        print('no')

    else:
        print('yes')