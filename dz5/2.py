#Необходимо создать три словаря и написать функцию, которая сможет брать словари и производить их слияние в один

def mergeDictionaries_MuscleCars():
    dict_1 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    dict_2 = {'brand': 'Dodge', 'model': 'Challenger', 'year': 1969}
    dict_3 = {'brand': 'Chevrolet', 'model': 'Camaro', 'year': 1967}
    print('Наш первый словарь:', dict_1)
    print('Второй словарь:', dict_2)
    print('Третий словарь:', dict_3)

    mergeDict = {**dict_1, **dict_2, **dict_3}
    print('Производим слияние трех словарей:', mergeDict)

mergeDictionaries_MuscleCars()