try:
    value = int(input("Enter a number: "))
    result = 10 / value
except Exception as e:
    print(f"An error occured: {e}")

print(f"{result}")
print("End program")