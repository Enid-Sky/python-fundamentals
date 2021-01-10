# Call .append() on an existing list to add a new item to the end
# With append you can add integers, dictionaries, tuples, floating points etc.
#


mixed = [1, 2]

mixed.append(3)  # integer

mixed.append("flour")  # string

mixed.append(5.0)  # float

mixed.append({"greeting": "hello"})  # dictionary

mixed.append((1, "hello", 5.0))  # tuple

print(f'mixed: {mixed}')
