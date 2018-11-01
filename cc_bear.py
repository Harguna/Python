'''for i in range(int(input())):
    a=input()
    count=0
    for j in range(len(a)):
        if a[j]=='1':
            count +=1
    if count==0:
        print('NO')
    else:
        if ('1'*(count)) in a:
            print('YES')
        else:
            print('NO')   '''

for i in range(int(input())):
    x=input().strip('0')
    if '0' in x or len(x)==0:
        print('NO')
    else:
        print('YES')