list = []
while True:
	print('''1. Add
2. Remove
3. Display
4. Quit''')
	choice = input("Enter choice: ")
	
	if choice == "1":
		try:
			num = int(input("Integer: "))
			list.append(num)
			print("List after adding:",list)
		except :
			print("invalid input")
	
	elif choice == "2":
			if not list:
				print("List is empty")
			else:
				try:
					num = int(input("Integer: "))
					if num in list :
						list.remove(num)
						print("List after removing:",list)
					else:
						print("Element not found")
				except:
					print("Invalid input")
	elif choice == "3":
		if not list:
			print("List is empty")
		else:
			print(list)
	elif choice == "4":
		break
	else:
		print("Invalid choice")
