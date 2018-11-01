opt= int(input("Enter 1 for number palindorme or 2 for string palindrome: "))

def no_palindrome(num):
	temp= num
	count=1


	while (temp//10) != 0:
		temp= int(temp/10)
		count= count + 1

	temp= num
	rev=0

	for i in range(0,count):
		temp2= divmod(temp,10)
		temp= temp2[0]
		rem= temp2[1]
		rev= rev+(10**(count-i-1))*rem

	if rev==num:
		print("The number is a palindrome")
	else:
		print("The number is not a palindrome")

def str_palindrome(str1):
	num=len(str1)


	for i in range(0,num):
		if i==0:
			str2= str1[num-1-i]
		else:
			str3=str1[num-i-1]
			str2= str2+ str3

	if str2==str1:
		print("String is a palindrome")
	else:
		print("String is not a palindrome")

if opt==1:
	num= int( input("Enter a number: "))
	no_palindrome(num)
	
if opt==2:
	str1= input("Enter the string: ")
	str_palindrome(str1)


