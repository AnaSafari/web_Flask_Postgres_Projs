def do_twice(func):
	def wrapper_do_twice():
		func()
		func()

	return wrapper_do_twice

@do_twice
def say_whee():
	print("Whee!")

print(say_whee())


# The solution is to use *args and **kwargs in the inner wrapper function. 
# Then it will accept an arbitrary number of positional and keyword arguments. 

