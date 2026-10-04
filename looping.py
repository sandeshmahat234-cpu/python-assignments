numbers = [2, -3, 4, -5, -6, 7, 8, -9]

count = 0
for num in numbers:
    if num < 0:
        count += 1

print("Number of negative numbers:", count)