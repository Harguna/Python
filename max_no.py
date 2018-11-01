num= int(input("Enter total number of elements: "))
arr= []

for i in range(0,num):
	arr.append(int(input("Enter element number %d: " %(i+1))))

#arr.sort()

#  or
def max_no(arr):
	for i in range(0,num-1):
		if arr[i]>arr[i+1]:
			temp=arr[i]
			arr[i]=arr[i+1]
			arr[i+1]=temp

print("Maximum value is: " + str(arr[num-1]))
