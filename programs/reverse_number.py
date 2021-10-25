def reversDigits(num):
	string = str(num)
	string = list(string)
	string.reverse()
	string = ','.join(string)
	
	return string

if __name__ == "__main__":

	num = int(input("enter a number"))
	print("Reverse of no. is ", reversDigits(num))

