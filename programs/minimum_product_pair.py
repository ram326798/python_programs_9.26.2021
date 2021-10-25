# Python program to
# calculate minimum
# product of a pair
def printMinimumProduct(arr,n):
	first_min = min(arr[0], arr[1])
	second_min = max(arr[0], arr[1])

	for i in range(2,n):
	
		if (arr[i] < first_min):
		
			second_min = first_min
			first_min = arr[i]
		
		elif (arr[i] < second_min):
			second_min = arr[i]
	
	return first_min * second_min
a= []
n = int(input("enter array length :"))
for i in range(0,n):
    a.append(int(input("Enter value")))

print(printMinimumProduct(a,n))

