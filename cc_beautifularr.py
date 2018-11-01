num=int(input())

def ba(a,n):
    ans='yes'
    for i in range(0,n):
        for j in range(1,n):
            if i!=j:
                if str(int(a[i])*int(a[j])) in a:
                    ans='yes'
                else:
                    ans='no'
    return (ans)

for i  in range(num):
    n=int(input())
    arr=input().split()
    if n==1:
        print('no')
    else:
        print(ba(arr,n))