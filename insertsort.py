size= int(input())
arr=[]
temp=input()
arr=temp.split()


num=int(arr[size-1])

for i in range(0,size-1):
    y=i
    ans=str(arr[0])
    if num<int(arr[size-2-i]):
        arr[size-1-i]=arr[size-2-i]
        
        
    if num>int(arr[size-2-i]):
        temp2=num
        num=arr[size-1-i]
        arr[size-1-i]=temp2
    
    for j in range(1,size):
        ans=ans+" "+str(arr[j])
    print(ans)

    
    if num<int(arr[0]) and y==size-2:
        ans=str(num)
        for j in range(1,size):
        	ans= ans+" "+str(arr[j])
        print(ans)
