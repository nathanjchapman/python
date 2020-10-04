# Write your first_three_multiples function here
def first_three_multiples(num):
	print(num, num*2, num*3)
	return num*3

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0



# Write your tip function here:
def tip(total, percentage):
	return total * (percentage / 100)
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0



# Write your introduction function here:
def introduction(first_name, last_name):
	return last_name + ", " + first_name + " " + last_name
# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou



# Write your dog_years function here:
def dog_years(name, age):
	return "{}, you are {} years old in dog years".format(name, age * 7)
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"



# Write your lots_of_math function here:
def lots_of_math(a,b,c,d):
	x = a+b
	y = c-d
	z = x*y
	print(x,y,z)
	return z % x
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
