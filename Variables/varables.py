# 5.4 Storing items invariables

# Variables can start with a letter (upper or lower) or an underscore
# Greeting = "'ello govner"
# greeting = "Hello"
# _myName = "Jamie"
#
# age = 24
# print(age)
#
# print(greeting + age)

# a = 12
# b = 3
# print(a + b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a // b)
# print(a % b)
#
# for i in range(1,(a//b)):
#     print(i)

# print(a + b / 3 - 4 * 12)
# print((((a+b)/3)-4)*12)


# 5.5 More about variables and strings

# c = a+b
# d = c/3
# e = d-4
# print(e*12)

parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])
print(parrot[-1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[0:6:2])

number = '9,223,372,063,854,775,807'
print(number[1::4])

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])

string1 = "he's "
string2 = "probably "
print(string1+string2)
print("he's " "probably " "pining")

print("Hello " *5)

today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)