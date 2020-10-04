# Write your sum_values function here:
def sum_values(obj):
	return sum(obj.values())

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6



# Write your sum_even_keys function here:
def sum_even_keys(obj):
	count = 0
	keys = obj.keys()
	for key in keys:
		if (key % 2 == 0):
			count += obj[key]
	return count

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6



# Write your add_ten function here:
def add_ten(obj):
	for k, v in obj.items():
		obj[k] += 10
	return obj

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}



# Write your values_that_are_keys function here:
def values_that_are_keys(obj):
	equal_values = []
	for k, v in obj.items():
		if v in obj.keys():
			equal_values.append(obj[k])
	return equal_values

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]



# Write your max_key function here:
def max_key(obj):
	return list(obj.keys())[list(obj.values()).index(max(obj.values()))]

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"



# Write your word_length_dictionary function here:
def word_length_dictionary(words):
	obj = {}
	for word in words:
		obj[word] = len(word)
	return obj

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}



# Write your frequency_dictionary function here:
def frequency_dictionary(words):
	frequency = {}
	for word in words:
		frequency[word] = words.count(word)
	return frequency

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}



# Write your unique_values function here:
def unique_values(obj):
	return len(set(obj.values()))

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1



# Write your count_first_letter function here:
def count_first_letter(names):
	keys = {}
	for last_name, first_names in names.items():
		if last_name[0] not in keys:
			keys[last_name[0]] = len(first_names)
		else:
			keys[last_name[0]] += len(first_names)
	return keys

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
