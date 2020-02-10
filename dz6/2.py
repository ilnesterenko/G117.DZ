#Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':645, 'b':3987, 'c': 093,'d':111, 'e':646, 'f': 20}

my_dict = {'a':645, 'b':3987, 'c': 93,'d':111, 'e':646, 'f': 20}
print('Так выглядит наш словарь: ', my_dict)

maxValue1 = max(my_dict, key=my_dict.get)
print('Ключ с самым высоким значением: ', maxValue1)
my_dict.pop(maxValue1)

maxValue2 = max(my_dict, key=my_dict.get)
print('Второй ключ с самым высоким значением: ', maxValue2)
my_dict.pop(maxValue2)

maxValue3 = max(my_dict, key=my_dict.get)
print('Третий ключ с самым высоким значением: ', maxValue3)
my_dict.pop(maxValue3)
