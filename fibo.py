frst=0
sec=1
num= int( input("Enter number of elements: ") )
sum1=0
count= 0
sum2=0

for i in range(0,num):
	if i==0:
		print(str(frst))

	elif i==1:
		print(str(sec))
		sum2=sec
	
	else:
		sum1= frst+ sec
		print(str(sum1))
		frst=sec
		sec= sum1
		sum2=sum2+sum1
		
print("Total=", sum2)
