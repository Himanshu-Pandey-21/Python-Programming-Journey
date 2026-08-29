try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ValueError:
    print("Error: Please enter valid integers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
