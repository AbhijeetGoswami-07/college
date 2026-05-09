import math
num = int(input())

if num >= 1 and num <= 9:
	print(num**2)
elif num >=10 and num <= 99:
	print(f"{math.sqrt(num):.2f}")
elif num >= 100 and num <= 999:
	print(f"{num ** (1/3):.2f}")
else:
	print("Invalid")
