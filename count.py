n= int(input())
arr= list()
for i in range (0,n):
    x= int(input())
    arr.append(x)

srt= sorted(arr)
print(srt)
i=0

new= []
while(i< n):
    count=0
    temp= int(srt[i])
##    new.append(temp)
    while(i<n and int(srt[i])==temp):
#        count= count+1
        i= i+1
#    print(str(srt[i-1])+ ':' + str(count))

##print(new)
