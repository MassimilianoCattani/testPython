print("Hello World!")

user_inp = input("Enter psw")


while(user_inp != "id1"):
	print(user_inp + " is not a valid psw!")
	print(input("Enter valid psw"))
	if(user_inp == "id1"):
		print("You are in")
