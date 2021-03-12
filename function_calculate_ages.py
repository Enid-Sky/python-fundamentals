def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


my_age = calculate_age(2021, 1986)
dads_age = calculate_age(2021, 1948)
moms_age = calculate_age(2021, 1954)

print(
    f"My mom's age is {moms_age}, my dads_age is {dads_age} and my age is {my_age}")
