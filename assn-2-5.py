#Convert Celsius to Fahrenheit
answer = "Y"
while answer.upper() != "N":
	while answer.upper() == "Y":
		degree = raw_input ("Are you converting from Celsius or from Fahrenheit? Please type C or F:")
		if degree.upper() == "C" :
			Celsius = float (raw_input("Enter degrees in Celsius:"))
			Fahrenheit = (Celsius * 9) / 5 + 32
			print "F", Fahrenheit
			answer = raw_input ("Would you like to convert another temperature? Please type Y or N:")
		elif degree.upper() == "F":
			Fahrenheit = float (raw_input("Enter degrees in Fahrenheit:"))
			Celsius = (Fahrenheit - 32) * .5556
			print "C", Celsius
			answer = raw_input ("Would you like to convert another temperature? Please type Y or N:")
		else :
			print "Please enter C or F"
if answer.upper() == "N":
	print "Thanks for using my program!"
else:
	print "Please enter Y or N"
