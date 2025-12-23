#functions in python!!
from ast import For


print("function without arguments")
def myfun(): #function definition
    print("welcome to mahek's code\n")

myfun() #function call


print("function with arguments")
def evenodd(x):
    """
    Docstring for evenodd
    this code will print whether the number is odd or even
    """
    if x%2==0:
        return "given number is even"
    else:
        return "given number is odd\n"
    
print(evenodd(356))
print(evenodd(987))

print("keyword arguments in python")
def keywordargument(fname,lname):
    """
     Docstring for myfun
     in this function we have used keyword
     
    """
    print("your first name is ", fname )
    print("your last name is ", lname)
keywordargument(fname="Mahek", lname="junnedi")
keywordargument(lname="junnedi", fname="Mahek")
print("\n")
      
print("positional arguments in python")
def positionalargument(name,age):
    """
    Docstring for positionalargument
    in this function we have used positional arguments
    """
    print("your name is ",name)
    print("your age is ", age)
positionalargument("Mahek",20)
positionalargument(20,"Mahek")

print("\n")

print("arbitary arguments in python")
def myfun(*args, **kwargs):
	print("non keyword *args:")
	for arg in args:
		print(arg)

	print("keyword **kwargs:")
	for key,value in kwargs.items():
		print(f"{key} == {value}") 
myfun("hello" , "Mahek" , course = "Internship" , Duration = "6 Months")

print("\n")

print("anonymous functions in python")
def cube(x) : return x*x*x   # without lambda
Cube_l = lambda x : x*x*x  # with lambda
print(cube(7))
print(Cube_l(7))

print("\n")

print("recursive functions in python")
def factorial(n):
    """
    Docstring for factorial
    this function will return the factorial of a number
    """
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))
print(factorial(7))