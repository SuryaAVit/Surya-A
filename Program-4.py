numbers = [1, 4, 9, 34, 17, 26, 47, 80, 13, 20, 40]

result = {}

for i in range(1, 10):
    count = 0
    for num in numbers:
        if num % i == 0:
            count += 1
    result[i] = count

print(result)
