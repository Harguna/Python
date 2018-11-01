str1= input("Enter the string: ")

def rev_str(str1):
	num=len(str1)
	for i in range(0,num):
		if i==0:
			str2= str1[num-1-i]
		else:
			str3=str1[num-i-1]
			str2= str2+ str3

	print(str2)

#str[::-1]
