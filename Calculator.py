num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

print("Choose the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponentiation")


choice = input("Enter choice(1/2/3/4/5/6): ")

match choice:
    case '1'| "+":
        print(num1, "+", num2, "=", num1 + num2)
    case '2'| "-":
        print(num1, "-", num2, "=", num1 - num2)
    case '3'| "*":
        print(num1, "*", num2, "=", num1 * num2)
    case '4'| "/":
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)    
        else:
            print("Invalid input")
    case '5'| "%":
        print(num1, "%", num2, "=", num1 % num2)
    case '6'| "**":
        print(num1, "**", num2, "=", num1 ** num2)
   
    case _:
        print("Please enter a valid choice")
