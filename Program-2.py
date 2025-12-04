a = int(input("Enter a: "))

result = []
for i in range(1, 2*a, 2):
    result.append(i)
print(*result, sep=(", "))
