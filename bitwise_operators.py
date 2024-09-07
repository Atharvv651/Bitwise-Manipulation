num1 = int(input("Enter Number One: "))
num2 = int(input("Enter Number Two: "))

print()

print("AND:")
print(f"{num1} & {num2} = {num1 & num2}")
print()

print("OR:")
print(f"{num1} | {num2} = {num1 | num2}")
print()

print("NOT:")
print(f"~{num1} = {~num1}")
print(f"~{num2} = {~num2}")
print()

print("XOR:")
print(f"{num1} ^ {num2} = {num1^num2}")
print()

print("RIGHT SHIFT:")
print(f"{num1} >> 2 = {num1>>2}")
print(f"{num2} >> 2 = {num2>>2}")
print()

print("LEFT SHIFT:")
print(f"{num1} << 2 = {num1<<2}")
print(f"{num2} << 2 = {num2<<2}")