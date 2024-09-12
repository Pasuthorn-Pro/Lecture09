def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Exception:", e)
    else:
        return result

a, b = map(int, input("Enter two number: ").split())
print(divide(a,b))
print("End Program")