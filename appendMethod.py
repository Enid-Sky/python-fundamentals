# Call .append() on an existing list to add a new item to the end
# With append you can add integers, dictionaries, tuples, floating points, and any objects.
# Python lists reserve extra space for new items at the end of the list. A call to .append() will place new items in the available space.


mixed = [1, 2]  # initial list

mixed.append(3)  # integer

mixed.append("flour")  # string

mixed.append(5.0)  # float

mixed.append({"greeting": "hello"})  # dictionary

mixed.append((1, "hello", 5.0))  # tuple

print(f'mixed: {mixed}')


# NOTE: Using append is equivalent to the following operation

# SLICE OPERATION:

numbers = [1, 2, 3]

numbers[len(numbers):] = 4

print(f'numbers: {numbers}')
