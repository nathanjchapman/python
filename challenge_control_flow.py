# Write your large_power function here:
def large_power(base, exponent):
	if (base**exponent) > 5000:
		return True
	else:
		return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False



# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
	if budget < (food_bill+electricity_bill+internet_bill+rent):
		return True
	else:
		return False
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True



# Write your twice_as_large function here:
def twice_as_large(num1, num2):
	if num1 > (num2*2):
		return True
	else:
		return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True



# Write your divisible_by_ten function here:
def divisible_by_ten(num):
	if (num / 10) and (num % 10 == 0):
		return True
	else:
		return False
# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False



# Write your not_sum_to_ten function here:
def not_sum_to_ten(num1, num2):
	if (num1 + num2) != 10:
		return True
	else:
		return False
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False