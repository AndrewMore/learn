try:
	score = float (raw_input (" Please enter a score:"))
	if score < 0.0 or score > 1.0 :
		print "Bad score"
	elif score >= 0.9 :
		print "A"
	elif score >= 0.8 :
		print "B"
	elif score >= 0.7 :
		print "C"
	elif score >= 0.6 :
		print "D"
	elif score < 0.6 :
		print "F"
except:
	print "Bad score"