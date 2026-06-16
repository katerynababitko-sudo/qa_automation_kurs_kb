# input a string
input_string = input("Enter a new string: ")

print(f"Your string is: ", input_string)

# convert input string into the list
input_list = list(input_string)

# then we convert it to set to get rid of the duplicates
input_set = set(input_list)

split_value = 10

if len(input_set) > split_value:
    print(f"The input string contains more than {split_value} unique elements. {True}")
else:
    print(f"The input string contains less than {split_value} unique elements. {False}")
