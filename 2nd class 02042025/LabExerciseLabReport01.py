num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

sum_of_numbers = num1 + num2 + num3

if num1 == num2 == num3:
    sum_of_numbers *= 3 

if sum_of_numbers % 2 == 0:
    print(f"The sum is {sum_of_numbers}, which is even.")
else:
    print(f"The sum is {sum_of_numbers}, which is odd.")
