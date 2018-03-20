

def demystify(l1_string):
	newString = ""
	for c in l1_string:
		if c == "l":
			newString = newString + "a"
		if c == "1":
			newString = newString + "b"
		else:
			pass
	return newString


print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))