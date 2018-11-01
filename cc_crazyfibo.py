num=int(input())
def fibo(x,y,temp,z):
    if z>2:
        j=2
        for i in  range(int(z)-2):
            t=arr[j]-arr[j-1]
            arr.append(t)
            j=j+1
    return (arr[len(arr)-1])
for i in range(num):
    arr=[]
    a,b,n= input().split()
    arr.append(0)
    arr.append(int(a))
    arr.append(int(b))
    print(int(fibo(int(a),int(b),arr,int(n)))%10000007)