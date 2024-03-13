types = [
	...,
	None,
	True, False, bool,
	1, int,  # sys.maxsize
	1.1, float,  # sys.float_info
	' ', " ", """ """, f'', r'', str,
	b'', bytes,
	[], list,
	(), tuple,
	{1, }, set,
	{}, dict
]


class CustomException(Exception):
	...


def return_tuple() -> tuple[int, ...]:
	pass


name, age = "Alex", 25
print(f"ello, my name is {name}. i’m {age}.")  # hello, my name is Alex. i’m 25.


class CustomException(Exception):
	...


def return_tuple() -> tuple[int, ...]:
	pass


my_str = "One 1 two 2 three 3 four 4 five 5 six 6789"
numbers = [i for i in my_str if i.isdigit()]
