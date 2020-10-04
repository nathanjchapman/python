#Write your function here
def every_three_nums(start):
	return list(range(start,101,3))

#Uncomment the line below when your function is done
print(every_three_nums(91))
		


#Write your function here
def remove_middle(lst, start, end):
	del lst[start:end+1]
	return lst

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))



#Write your function here
def more_frequent_item(lst, item1, item2):
	if lst.count(item1) >= lst.count(item2):
		return item1
	else:
		return item2

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))



#Write your function here
def double_index(lst, index):
	# Checks to see if index is too big
	if index >= len(lst):
		return lst
	else:
		# Gets the original list up to index
		new_lst = lst[0:index]
		# Adds double the value at index to the new list 
		new_lst.append(lst[index]*2)
		#  Adds the rest of the original list
		new_lst = new_lst + lst[index+1:]
		return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))



#Write your function here
def middle_element(lst):
	if len(lst) % 2 != 0:
		middle = (len(lst) % 2) + 1
		return lst[middle]
	else:
		half = len(lst) // 2
		mid_1 = lst[half - 1]
		mid_2 = lst[half]
		return (mid_1 + mid_2) / 2

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
