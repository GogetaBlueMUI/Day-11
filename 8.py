def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))
result = divide_numbers(num1, num2)
print("The result is:", result)
