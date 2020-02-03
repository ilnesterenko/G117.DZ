import random

def helloFunction(rangeOfList, maxValueOfList):

    list = [random.randint(0, maxValueOfList) for i in range(rangeOfList)]
    print('Ваш список: ', list)


helloFunction(int(input('Определите длину списка: ')), int(input('Максимально возможное значение элемента списка: ')))







