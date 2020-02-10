#Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':645, 'b':3987, 'c': 093,'d':111, 'e':646, 'f': 20}

my_dict = {'a':645, 'b':3987, 'c': 93,'d':111, 'e':646, 'f': 20}
print('Так выглядит наш словарь: ', my_dict)

highestValue1 = max(my_dict, key=my_dict.get)
print('Ключ с самым высоким значением: ', highestValue1)
my_dict.pop(highestValue1)

highestValue2 = max(my_dict, key=my_dict.get)
print('Второй ключ с самым высоким значением: ', highestValue2)
my_dict.pop(highestValue2)

highestValue3 = max(my_dict, key=my_dict.get)
print('Третий ключ с самым высоким значением: ', highestValue3)
my_dict.pop(highestValue3)
