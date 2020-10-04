def title_decorator(print_name_function):
	def wrapper(*args, **kwargs):
		print("Professor:")
		print_name_function(*args, **kwargs)
	return wrapper

@title_decorator
def print_name(name, age):
	print(name + " you are " + str(age))

print_name("Charles", 25)
