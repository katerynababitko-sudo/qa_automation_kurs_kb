initial_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", 0.2, 9.5]

list_only_even_numbers = []

for element in initial_list:
    if isinstance(element, int) and element % 2 == 0:
        list_only_even_numbers.append(element)

print(f"The new list with only even numbers is: {list_only_even_numbers}")

sum_of_even_elements = sum(list_only_even_numbers)

print(f"The total sum of all even elements is: {sum_of_even_elements}")

