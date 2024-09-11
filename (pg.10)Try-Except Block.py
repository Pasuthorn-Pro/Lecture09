#Syntax
#try:
#   Code that may raise an exception
#except ExceptionType:
#   Code to handle the exception

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

print("End program")