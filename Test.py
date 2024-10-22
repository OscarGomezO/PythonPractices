
def is_prime(num):
	if num == 1 or num == 0:
		return False
	elif num == 2:
		return True
	else:
		for i in range (2, num):
			if num % 2 == 0:
				return False
			elif num % i == 1 and i == num-1:
				return True


for i in range(1, 20):
	if is_prime(i):
		result = is_prime(i)
		print(i,result, end=" ")



                     
#print(is_prime(1))
