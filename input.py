import sys
name= input("Enter the name: ")
frst_name=name.split(' ')[0]
sur_name=name.split(' ')[1]
prof= input("Enter your profession: ")
rank=input("Enter the rank: ")
nat= input("Nationality: ")
ht= input("Height is: ")
wt= input("Enter the weight: ")
print(" ")
print ("Data saved !")
print("\n")

num1=int( input("Press 1 to know about "+ name + " or 0 to quit: ") )

if  num1==1:
	print( "This is about: " + frst_name + " "+sur_name)
	print("He belongs to: " + prof)
	print("He is currently ranked as " + rank)
	print("His nationality is: " + nat)
	print("His weight is " + str(80) + " kg")
	print("His stands " + ht[0] + " feet and " + ht[2] + " inches tall" ) 
	
if  num1== 0:
 	sys.exit()
 	

