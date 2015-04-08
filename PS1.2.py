# PS-1.2
# COUNTING BOBS

s = raw_input("Enter a string: ")
numBobs = 0

for char in range(1, len(s)-1):
	if s[char-1: char+2] == "bob":
	#if char == "bob":
		numBobs += 1
print "Total number of Bobs= " +str(numBobs)
