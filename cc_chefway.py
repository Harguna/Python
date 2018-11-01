'''last,limit=input().split()
street=input().split()
ans=int(last)
arr=[]

def check():
    for i in range(1,int(last)):
        if int(last)-1-i == limit:
            arr.append(street[i])
        elif int(last)-1-i > limit:

i=1
while i< int(last):
    if (int(last) - 1-i) % int(limit) == 0:
        multiple()
    else:
        if int(last)-1-i <= limit:
            arr.append(street[i])
            i=int(last)
        elif int(last)-1-i > limit:'''

last,limit=input().split()
street=input().split()

extra= int((int(street[int(last)-1])-int(street[0]))%int(limit))
print(extra)
i=extra
ans=int(street[0])

while(i<=int(last)):
    ans = ans * int(street[i])
    i=i+int(limit)

print(ans%1000000007)