# PS-1.3
# ALPHABETICAL SUBSTRINGS

s = raw_input("Enter a string: ")
maxSub, currentSub, previousChar = '', '', ''

for char in s:
	if char >= previousChar:
		currentSub += char
	if len(currentSub) > len(maxSub):
		maxSub = currentSub
	else:
		currentSub = char
	previousChar = char
print maxSub
