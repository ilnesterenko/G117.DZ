#Нужно написать функцию, которая будет считать сколько раз символ встречается в строке.
#Например, в строке "Денис даёт нам классные задачки, которые помогут нам найти лучшую работу!" символ "е" встречается 3 раза.

def countCharacters(checkedString, searchСhar):

    for i in searchСhar:
        charCounter = checkedString.count(i)
    if charCounter >= 1:
        print('Искомый символ:', i, '. Встречается в строке раз:', charCounter)

countCharacters(str(input('Введите строку, в которой хотите посчитать одинаковые символы: ')),
                    str(input('Введите искомый символ: ')))