r = int(input())
for i in range(0, r):
    arr=[]
    temp=[]
    l=int(input())
    temp=input()
    if temp[0]=='T':
        print('Invalid')
    else:
        for i in range(0, l):
            if temp[i]!='.':
                arr.append(temp[i])

        count_h=0
        count_t=0
        count=0
        for i in range(0,len(arr)):
            if arr[i]=="T":
                count_t=count_t+1
            else:
                count_h= count_h+1

        if count_h!=count_t:
            print('Invalid')
        else:
            for i in range(0, len(arr)-1):
                if arr[0]=="T":
                    count=1
                else:
                    if ((arr[i]=="T" and arr[i+1]!="H") or (arr[i]=="H" and arr[i+1]!="T")):
                        count=1
            if count==0:
                print('Valid')
            elif count==1:
                print('Invalid')