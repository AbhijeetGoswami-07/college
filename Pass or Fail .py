n = int(input())
marks = list(map(int,input().split()))

if any(m<40 for m in marks):
	print("Fail")
else :
	per =sum(marks) / n
	print(f"Aggregate Percentage: {per:.2f}")
	if per > 75 :
		print("Grade: Distinction")
	elif per >= 60 :
		print("Grade: First Division")
	elif per >= 50 :
		print("Grade: Second Division")
	elif per >= 40 :
		print("Grade: Third Division")
