cases = int(input())
for i in range(cases):
    num = int(input())
    val = input().split()
    val=list(map(int, val))
    ans=False
    l=len(val)
    x=int(l/ 2)

    def check():
        temp=val[0]
        p=False
        for j in val[1:x-1]:
            if (j==temp or j-1==temp):
                p=True
                temp=j
            else:
                p=False
                break
        if (p and val[x-1]==6 and val[0]==1):
            return True
        else:
            return False

    if (l>=13):
        if (l%2 != 0):
            if val[x] == 7:
                if val[0:x] == val[l:x:-1]:
                    if check():
                        ans=True
        else:
            
    if(ans):
        print('yes')
    else:
        print('no')
