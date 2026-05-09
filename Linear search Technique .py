arr = list(map(int,input().split()))
key = int(input())

val = False

for i in range(len(arr)):
	if arr[i] ==key :
		print(i)
		val = True
		break
if not val:
	print("Not found")

