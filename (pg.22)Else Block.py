#try:
#   Code that may raise except
#except ExceptionTtpe:
#   Code to handle the exception
#else:
#   Code to execute if no exceptions were raised

try:
    value = int(input("Enter a number: "))
    result = 10 / value
except:
    print("Cannot divide by zero!")
else:
    print(f"The result is: {result}")

print("End program")