number = 234
result = 0
for i in bin(number)[2:]:
    if i == '1':
        result += 1
print(result)

# -----------------------------------
number = 234
binary = bin(number)
binary = binary[2:]
print(binary.count('1'))
