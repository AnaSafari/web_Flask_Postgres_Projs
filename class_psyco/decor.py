def parent(num):
	def first_child():
		return "Hi, I'm the first child"

	def second_child():
		return "Hi,I am the second child"

	if num == 1:
		return first_child
	else:
		return second_child


first = parent(1)
second = parent(2)

print(first)
print(second)

print(first())
print(second())


def parentm(num):
	def first_child():
		return "Hi, I'm the first child"

	def second_child():
		return "Hi,I am the second child"

	if num == 1:
		return first_child()
	else:
		return second_child()


first = parentm(1)
second = parentm(2)

print(first)
print(second)
