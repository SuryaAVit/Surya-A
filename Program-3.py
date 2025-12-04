a = int(input("Enter a: "))
n = (a + 1) // 2

result = []
for i in range(n):
    result.append(str(2 * i + 1))

print(*result, sep=", ")
