#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.

print("Simple Calculator")
print("Operations are : ")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

# For input choice
choice = input("Enter your choice: ")
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if choice == '1':
    print(x + y)
elif choice == '2':
    print(x - y)
elif choice == '3':
    print(x * y)
elif choice == '4':
    print(x / y)  
else:          
    print("Invalid choice")