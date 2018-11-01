#exception handling
try:
    a = int(input("Enter any number :"))
    print("Inside try block")
    b = 20/a
    print(b)
except ValueError:
    print("Enter number only")
except ZeroDivisionError:
    print("Zero is not supported")
except:
    print("Exception")
finally:
    print("pROGRAM NOW ENDS")

#file handling
a= open("file.txt",'w')
b="Successfully written"
a.write(b)

c=len(b)
print(c)
a.seek(20,0)
e=a.tell()
print(e)
