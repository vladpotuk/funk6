def count_digits(number):
    number_str = str(number)
    count = len(number_str)
    return count
my_number = 3456
result = count_digits(my_number)
print(f"Кількість цифр у числі {my_number}:{result}")
