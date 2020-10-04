# Write your in_range function here:
def in_range(num, lower, upper):
	if (num >= lower) and (num <= upper):
		return True
	else:
		return False
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False



# Write your same_name function here:
def same_name(your_name, my_name):
	if (your_name == my_name):
		return True
	else:
		return False
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False



# Write your always_false function here:
def always_false(num):
	if (num > num):
		return False
	else:
		return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False



# Write your movie_review function here:
def movie_review(rating):
	if rating <= 5:
		return "Avoid at all costs!"
	elif rating in range(5,9):
		return "This one was fun."
	elif rating >= 9:
		return "Outstanding!"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."



# Write your max_num function here:
def max_num(num1, num2, num3):
	largest = max(num1, num2, num3)
	if (num1 == num2) and (num1 >= largest):
		return "It's a tie!"
	elif (num1 == num3) and (num1 >= largest):
		return "It's a tie!"
	elif (num3 == num2) and (num2 >= largest):
		return "It's a tie!"
	else:
		return largest
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
