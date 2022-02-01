# In python data type is set when u assign a value to a variable
x = "Hello World"
print (type(x))

x = 1
print (type(x))  #for integers no need to assign "" commas 

x = 20.5	#float	

x = 1j	#complex

x = ["apple", "banana", "cherry"]	#list

x = ("apple", "banana", "cherry")	#tuple	

x = range(6)   #range	

x = {"name" : "John", "age" : 36}	#dict

x = {"apple", "banana", "cherry"}	#set	

x = frozenset({"apple", "banana", "cherry"})	#frozenset	

x = True	#bool

x = b"Hello"	#bytes	


x = bytearray(5)	#bytearray	

x = memoryview(bytes(5))	#memoryview