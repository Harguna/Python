num= int( input("Enter number of entries: ") )
name=[]
count =0

for i in range (0,num):
	arr= input("Enter %d entry: " %(i+1))
	name.append(arr)

for k in range(0,num):
	print(name[k])
	
num2=int( input("Press 1 to check directory or 0 to finish: ") )

if num2==1:
	str1= input("Enter the name: ")
	print(str1)
	for  j in range(0,num):
 		if name[j] == str1:
 			count= count +1 

	if count==1: 
		print("Name exists !")

	else :
		print("Name does  not exist")
	
elif num2==0:
	input()

