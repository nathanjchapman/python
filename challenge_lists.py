#Write your function here
def append_sum(lst):
	count = 0
	while count < 3:
		count += 1
		added = lst[-1] + lst[-2]
		lst.append(added)
	return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))



#Write your function here
def larger_list(lst1, lst2):
	if len(lst1) >= len(lst2):
		return lst1[-1]
	else:
		return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))



#Write your function here
def more_than_n(lst, item, n):
	if lst.count(item) > n:
		return True
	else:
		return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))



#Write your function here
def append_size(lst):
	lst_len = len(lst)
	lst.append(lst_len)
	return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))



#Write your function here
def combine_sort(lst1,lst2):
	csl = lst1 + lst2
	csl.sort()
	return csl

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
