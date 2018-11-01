cars=[]
print("Enter 3 cars")
for i in range(0,3):
	cars.append(input())

num=int(  input("Press 1 to delete or Press 2 to add or Press 3 to replace or Press 4 to insert: "))

if num==1:
	str1= input("Name car to be deleted: ")
	cars.remove(str1)

if num==2:
	str1= input("Enter the new car: ")
	cars.append(str1)

if num==3:
	num2= int( input("Enter location: "))
	str2= input("Enter the new car: ")
	cars[(num2-1):num2]= [str2]

if num==4:
	num= int( input("Enter location: ") )
	str1= input("Enter new car: ")
	cars.insert((num-1),str1)

print(cars)
