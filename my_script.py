import time
from random import random


def list_without_comprehension():
	l = []
	for i in range(1000000):
		l.append(int(random() * 100 % 100))
	return l


def list_with_comprehension():
	# 1K random numbers between 0 to 100
	l = [int(random() * 100 % 100) for _ in range(1000000)]
	return l


# operations on list_without_comprehension
def sort_list_without_comprehension():
	list_without_comprehension().sort()


def reverse_sort_list_without_comprehension():
	list_without_comprehension().sort(reverse=True)


def sorted_list_without_comprehension():
	sorted(list_without_comprehension())


# operations on list_with_comprehension
def sort_list_with_comprehension():
	list_with_comprehension().sort()


def reverse_sort_list_with_comprehension():
	list_with_comprehension().sort(reverse=True)


def sorted_list_with_comprehension():
	sorted(list_with_comprehension())


if __name__ == "__main__":
	start_time = time.time()

	sort_list_without_comprehension()
	reverse_sort_list_without_comprehension()
	sorted_list_without_comprehension()

	sort_list_with_comprehension()
	reverse_sort_list_with_comprehension()
	sorted_list_with_comprehension()

	print("--- %s seconds ---" % (time.time() - start_time))
