# Write your square_root function here:
def square_root(num):
  return num ** 0.5
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10



# Write your win_percentage function here:
def win_percentage(wins, losses):
	return wins / (wins + losses) * 100.0
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100



# Write your average function here:
def average(num1, num2):
	return (num1 + num2) / 2
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0



# Write your remainder function here:
def remainder(num1, num2):
	return (num1 * 2) % (num2 / 2)
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0
