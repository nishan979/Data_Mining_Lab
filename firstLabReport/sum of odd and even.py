# Write a Python program to find the sum of odd and even numbers from a set of numbers.
num = [1, 2, 3, 4, 5, 6, 7, 8]
odd_sum = 0
even_sum = 0

for i in num:
    if i % 2 != 0:
        odd_sum += i
    else:
        even_sum += i

print(f"Sum of odd numbers: {odd_sum}")
print(f"Sum of even numbers: {even_sum}")
