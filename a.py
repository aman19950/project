x = [
    [1, 2, 3], 4, [34, 2, 1]
]

# print(list(map(max, x)))
z = []
for i in x:
    z.append(max(i))
print(z)
