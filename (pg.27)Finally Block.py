#try:
    # code that may raise an exception
#except ExceptionType:
    # code to handle the exception
#finally:
    # code to execute regardless of exceptions

try:
    # Ask user to input two numbers
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    # Perform the division
    result = numerator / denominator
    print(f"The result is: {result}")

except ZeroDivisionError:
    # Handle division by zero error
    print("Error: You cannot divide by zero.")

except ValueError:
    # Handle input error (if input is not a valid number)
    print("Error: Invalid input. Please enter numeric values.")

finally:
    # This block will always run, regardless of errors
    print("Execution completed, whether an exception occurred or not.")

print("End of program")
