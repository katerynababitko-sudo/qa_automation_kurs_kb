input_string = input("Enter a test string: ")

print(f"Your string is: ", input_string)


while "h" not in input_string.lower():
    input_string = input("No \"h\" was found in your input string. Please enter another one:  ")
print("Now you have entered the string with h ot H.")
