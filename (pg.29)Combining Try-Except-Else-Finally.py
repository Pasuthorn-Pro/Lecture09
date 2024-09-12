#try:
    # code that may raise an exception
#except ExceptionType:
    # code to handle the exception
#else:
    # code to execute if no exceptions were raised
#finally:
    # code to execute regardless of exceptions

try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"The resulr is: {result}")
finally:
    print("Execute is completed")