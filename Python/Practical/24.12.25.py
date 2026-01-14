# exception handling
try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")    

# handling multiple exceptions
try:
    n = 0
    res = 100 / n
except ZeroDivisionError: 
    print("You cant divide by zero!") 
except ValueError:    
    print("Enter a valid number!") 
else:     
    print("result  is",res)
finally:     
    print("Execution complete.")

# handling specific exceptions
try:
    x=int("str")  #this will give valueErroe since str cant be converted into integer 
    inv=1/x    #since x has no value, this will cause ZeroDivisionError 
except ValueError:     
    print("notvalid") 
except ZeroDivisionError:     
    print("zero value, cant solve")

#catching multiple exceptions in one block
a=["10","twenty",30]   #mixed int andn str
try:
    Total = int(a[0]) + int(a[1])   #twenty cannot be converted into int 
except (ValueError, TypeError) as e:
    print("error",e) 
except IndexError:     
    print("Index out of range.")

# raising exceptions
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:
        print("Valid age:", age)

try:
    check_age(-5)
except ValueError as e:
    print("Caught an error:", e)

# custom exceptions
class NegativeAgeError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative.")
    else:
        print("Valid age:", age)

try:
    validate_age(-10)   
except NegativeAgeError as e:
    print("Caught a custom error:", e)


#file handling

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
else:
    print(content)
try:
    with open("example.txt", "w") as file:
        file.write("Hello, World!")
    print("File written successfully.")
except IOError:
    print("An error occurred while writing to the file.")
try:
    with open("example.txt", "r") as file:
        content = file.read()
    print("File read successfully.")
    print(content)
except IOError:
    print("An error occurred while reading the file.")
try:
    with open("example.txt", "a") as file:
        file.write("\nAppending a new line.")
    print("File appended successfully.")
except IOError:
    print("An error occurred while appending to the file.")
try:
    import os
    os.remove("example.txt")
    print("File deleted successfully.")
except FileNotFoundError:
    print("File not found. Cannot delete.")
except IOError:
    print("An error occurred while deleting the file.")
