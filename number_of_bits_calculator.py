number = int(input("Enter a number: "))

binary = bin(number)

print(f"Binary Conversion: {binary}")
print(f"Count: {binary.count('1')}")