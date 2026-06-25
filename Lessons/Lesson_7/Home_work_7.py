# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 9:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_of_two(number_1: int, number_2: int) -> int:
     return number_1 + number_2

print("Task 2: " + str(sum_of_two(3, 4)))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean (*args) -> float:
    numbers = [k for k in args]
    quantity_of_numbers = len(numbers)

    return sum(numbers) / quantity_of_numbers

print("Task 3: " + str(arithmetic_mean(1, 2, 3, 4, 5)))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def str_reverse(string_value: str) -> str:
    # create a list from string
    list_of_string = [k for k in string_value]
    list_of_string.reverse()
    reversed_string = "".join(list_of_string)

    return reversed_string

print("Task 4: " + str_reverse("Test_task_4"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def get_longest_word(*args) -> str:
    list_of_arguments = [k for k in args]
    longest_word = max(list_of_arguments, key=len)

    return longest_word

print("Task 5: " + get_longest_word("Ab", "Ab", "Abc"))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2) -> int:
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print("Task 6a: " + str(find_substring(str1, str2))) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print("Task 6b: " + str(find_substring(str1, str2))) # поверне -1

# task 7

def get_sum_only_even_numbers(*args) -> int:
    """
    Returns the sum of all even integers from the given arguments.
    :param args: Variable number of arguments of any type.
    :return: int: Sum of even integers only. Non-integers are ignored.
    """
    initial_list = [k for k in args]
    list_only_even_numbers = []

    for element in initial_list:
        if isinstance(element, int) and element % 2 == 0:
            list_only_even_numbers.append(element)
    sum_of_even_elements = sum(list_only_even_numbers)
    return sum_of_even_elements

print("Task 7: " + str(get_sum_only_even_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", 0.2, 9.5)))


# task 8
def add_str_to_list(*args) -> list:
    """
    Extracts and returns only string values from the given arguments.
    :param args: Variable number of arguments of any type.
    :return: A list containing only elements of type str.
    """
    list_1 = [k for k in args]
    list_2 = []
    for element in list_1:
        if isinstance(element, str):
            list_2.append(element)

    return list_2

print("Task 8: " + str(add_str_to_list('1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum')))


# task 9
def get_rid_of_duplicates(*args) -> list:
    """
    Removes duplicate values from the given arguments.
    :param args: Variable number of arguments of any type.
    :return: A list containing unique elements.
    """
    initial_list = [k for k in args]
    set_without_duplicates = set(initial_list)

    return list(set_without_duplicates)

print("Task 9: " + str(get_rid_of_duplicates('1', '2', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum')))


# task 10
def check_element_in_string(initial_str: str, element: str) -> bool:
    """
    Checks if a substring exists within a string (case-insensitive).
    :param initial_str: The string to search in.
    :param element: The substring to find.
    :return: True, if substring is found
    """
    return element.lower() in initial_str.lower()

print("Task 10: " + str(check_element_in_string("test_string", "t")))