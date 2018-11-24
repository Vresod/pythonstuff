count = int(input("What number are we fizzbuzzing to? "))

for i in range(1,count + 1):
	output = ""
	if (i % 3 == 0):
		output += "fizz"
	if (i % 5 == 0):
		output += "buzz"
	if (output == ""):
		output = i
	print(output)