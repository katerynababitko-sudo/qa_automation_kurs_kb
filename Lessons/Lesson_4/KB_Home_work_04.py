adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
string_task_1 = adwentures_of_tom_sawer.replace("\n", " ")
print(f"The 1st string is -->\n" + string_task_1, "\n")

# task 02 ==
""" Замініть .... на пробіл
"""
string_task_2 = adwentures_of_tom_sawer.replace("....", " ")
print(f"The 2nd string without ... is -->\n" + string_task_2, "\n")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
string_task_3 = adwentures_of_tom_sawer.replace(" ", "")
print(f"The 3rd string without spaces is --> \n" + string_task_3, "\n")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
string_task_4 = str(adwentures_of_tom_sawer.count("h"))
print(f"The 4th solution: string contains --> " + string_task_4 + " letters 'h'. \n")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
list_task_5 = adwentures_of_tom_sawer.split()
count_task_5 = sum(1 for word in list_task_5 if word[0].isupper())
print(f"The 5th solution: string contains words with Capital Letter --> " + str(count_task_5) + "\n")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
position_1_task_6 = adwentures_of_tom_sawer.find("Tom")  # position of 1st find of Tom
position_2_task_6 = adwentures_of_tom_sawer.find("Tom", position_1_task_6 + 1)

print(f"The 6th solution: word 'Tom' is med 2nd time on position --> {position_2_task_6}. \n")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None

adwentures_of_tom_sawer_sentences = string_task_2.split(".")  # I have used the string from task 2 without ....
# i have a question here: i got the last element of the list as empty '', i do not get how it was produced
print(f"The 7th solution: a new list with separate sentences are defined as list elements --> \n"
      f"{adwentures_of_tom_sawer_sentences}. \n")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
string_task_8 = adwentures_of_tom_sawer_sentences[3].lower()

print(f"The 8th solution: the 4th sentence in lower register --> \n {string_task_8} \n")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
position_task_9 = adwentures_of_tom_sawer.find("By the time")
if position_task_9 >= 0:
    print(f"Solution for task 9: The combination 'By the time' was found at least once\n")
else:
    print(f"Solution for task 9: The combination 'By the time' was not present in the text. \n")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
string_task_10 = adwentures_of_tom_sawer_sentences[-1]
counter = len(string_task_10)
print(f"Solution for task 10: The last sentence has {counter} words. \n")
# --> i have here 0, because of empty element list from task 07
