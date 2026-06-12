# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
# 1st task: adding a new record to the list
new_record = ('Kateryna', 'Bidenko', '35', 'Kharkiv')

people_records.insert(0, new_record)
print(f"A new record is added at the 1st position: {people_records} \n")

# 2nd task: swap the elements with indexes 1 and 5
people_records[1], people_records[5] = people_records[5], people_records[1]
print(f"The records on position 2 and 6 are switched: {people_records} \n")

# 3rd task:
helper_list = [people_records[6][2], people_records[10][2], people_records[13][2]]

# 1st solution
if (int(people_records[6][2]) >= 30 and
        int(people_records[10][2]) >= 30 and
        int(people_records[13][2]) >= 30):
    print(f"True. The age of record 6, 10 and 13 is >= 30")
else:
    print(f"False. Some of the records on the position: (6, 10, 13) has age < 30")


# 2nd solution
def check_age(check_list):
    for element in check_list:
        if element < 30:
            return False
    return True


print(f"If the age for all items in specifies list {helper_list} are >= 30 we will get True, otherwise False. "
      f"For out list it is: {check_age(helper_list)}")

