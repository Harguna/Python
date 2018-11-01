num= int( input("Enter a number: "))
def rev_no(num):
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

	print(str(rev))

rev_no(num)
