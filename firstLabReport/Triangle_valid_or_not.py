# write a python program to Check Triangle is Valid or Not

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

if a + b > c and a + c > b and b + c > a:
    print("The given sides form a valid triangle.")
else:
    print("The given sides don't form a valid triangle.")




