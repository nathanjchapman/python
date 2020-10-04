#Write your function here
def divisible_by_ten(nums):
	count = 0
	for num in nums:
		if num % 10 == 0:
			count += 1
	return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))



#Write your function here
def add_greetings(names):
	greeting = []
	for name in names:
		greeting.append("Hello, " + name)
	return greeting

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))



#Write your function here
def delete_starting_evens(lst):
	while (len(lst)) and (lst[0] % 2 == 0):
		lst = lst[1:]
	return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))



#Write your function here
def odd_indices(lst):
	new_list = []
	for index in range(1, len(lst), 2):
		new_list.append(lst[index])
	return new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))



#Write your function here
def exponents(bases, powers):
	new_list = []
	for base in bases:
		for power in powers:
			new_list.append(base**power)
	return new_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))



#Write your function here
def larger_sum(lst1, lst2):
	if sum(lst1) >= sum(lst2):
		return lst1
	else:
		return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))



#Write your function here
def over_nine_thousand(lst):
	sum = 0
	for i in lst:
		if sum > 9000:
			break
		else:
			sum += i
	return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))



#Write your function here
def max_num(nums):
	return max(nums)	

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))



#Write your function here
def same_values(lst1, lst2):
	new_list = []
	for i in range(len(lst1)):
		if lst1[i] == lst2[i]:
			new_list.append(i)
	return new_list

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))



#Write your function here
def reversed_list(lst1, lst2):
	for index in range(len(lst1)):
		if lst1[index] != lst2[len(lst2) - 1 - index]:
			return False
	return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
