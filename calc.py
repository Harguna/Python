print("Press: 1 for even-odd ")
print("Press: 2 for prime number  ")
print("Press: 3 for factorial ")
print("Press: 4 for average ")
print("\n")

opt= int( input ("Enter your option: "))

def even_odd(num1):
	if num1==0: 
		print("Number is neither even nor odd")
	if num1%2==0:
		print("Number is even")
	else:
		print("Number is odd")

def prime_no(num2):
	count=0
	if num2==0|num2==1:
		print("Number is neither prime nor composite")
	for i in range(2,num2):
		if num2%i ==0:
			count= count+1
	if count>=1:
		print("Number is composite")
	else:
		print("Number is prime")

def fact(num3):
	fact =1
	while num3!=1:
		fact= num3*fact
		num3=num3 -1
	print("Factorial is: " + str(fact))

def avg(num4):
	add=0
	arr= []
	for j in range(0,elts):
		num4= int( input() )
		arr.append(num4)
		add=add + num4
	avg= float (add/elts)
	print( "Average is: " + str(avg) )

if opt==1:
	num1= int( input("Enter your number: ") )
	even_odd(num1)
	
elif opt==2:
	num2= int( input("Enter the number: ") )
	prime_no(num2)

elif opt==3:
	num3= int( input("Enter the number: ") )
	fact(num3)

elif opt== 4:
	elts= int( input("Enter the number of elements: ") )
	avg(elts)

else :
	print("Entered number does not match options !")

input("Press any key to finish")

a=20
def abc(a):

