def mydecorator(func):
	def wrapper():
		print("something is happening before func call")
		func()
		print("something is happening after func call")
		# print("hi")


	return wrapper


def say_Whee():
	print("Whee!")

say_Wheed = mydecorator(say_Whee)

print(f"this is {say_Wheed()}")

print("------------")
print(say_Whee)

print(",,,,,,,,,,,,,,,,")
print(say_Wheed)

print(">>>>>>>>>>>>>>>")
print(say_Wheed())
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
##############Doing the same thing as above using decorators
def my_decorator(func):
	def wrapper():
		print("something is happening before func call")
		func()
		print("something is happening after func call")

	return wrapper

@my_decorator
def say_Whee():
	print("Whee!")
