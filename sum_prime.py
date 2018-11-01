num= int( input("Enter number of prime numbers: ") )
count=0
add=0


def isPrime(x):
	ct=0
	for j in range(2,x):
		if x%j==0:
			ct= ct+1
	if ct==0:
		return True
		ct=0
	else:
		return False

for i in range(2,100):
	
	if count==num:
		 break
	elif i==2:
		count= count+1
		add= add+i
		print(str(i))
	else:
		if isPrime(i):
			count=count+1
			add= add+i 
			print(str(i))

print("Sum is: " + str(add))








#num= int( input("Enter the number of prime numbers: ") )
#count=0
#add=2

#while count!=num:
#	for i in range(3,100): 
#		print("Start: %d" %i)
#		for j in range(2,i):
#			if (i%j)!=0:
#				count= count+1
#				add= add+i
#				print("Count" + str(count))
#				print(i)
#			else: print("no")
			

#print("Sum is: " + str(add))



#		for j in range(2,i):
#			if (i%j)==0:
#				ct= ct+1
#		if ct==0:
#			add= add+i
#			count=count+ 1
#			ct=0
#			print(str(i))







