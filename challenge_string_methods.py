letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
	count = 0
	for l in letters:
		if l in word:
			count += 1
	return count

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4



# Write your count_char_x function here:
def count_char_x(word, x):
	count = 0
	for i, l in enumerate(word):
		if x == word[i]:
			count += 1
	return count
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1



# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
	count = 0
	length = len(x)
	for i, l in enumerate(word):
		if x == word[i:length + i]:
			count += 1
	return count
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1



# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
	if (start in word) and (end in word):
		s = word.find(start) + 1
		e = word.find(end)
		return word[s:e]
	else:
		return word

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"



# Write your x_length_words function here:
def x_length_words(sentence, x):
	words = sentence.split(" ")
	for word in words:
		if x != len(word):
			return False
		else:
			return True
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True



# Write your check_for_name function here:
def check_for_name(sentence, name):
	if name.lower() in sentence.lower():
		return True
	else:
		return False

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False



# Write your every_other_letter function here:
def every_other_letter(word):
	return word[::2]
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 



# Write your reverse_string function here:
def reverse_string(word):
	return word[-1::-1]
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print



# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
	first_letter1 = word1[0]
	first_letter2 = word2[0]
	new_word1 = first_letter2 + word1[1:]
	new_word2 = first_letter1 + word2[1:]
	return new_word1 + " " + new_word2
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a



# Write your add_exclamation function here:
def add_exclamation(word):
	while len(word) < 20:
		word += '!'
	return word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn