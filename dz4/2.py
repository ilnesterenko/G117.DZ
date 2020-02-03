import random

def helloFunction(rangeOfList, maxValueOfList):

    list = [random.randint(0, maxValueOfList) for i in range(rangeOfList)]
    print('Ваш список: ', list)
    list2 = [k for k in list if k > 7]
    print('Ваш список с числами больше 7: ', list2)

helloFunction(int(input('Определите длину списка: ')), int(input('Максимально возможное значение элемента списка: ')))







