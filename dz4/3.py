import random

def helloFunction(rangeOfList, maxValueOfList):

    list1 = [random.randint(0, maxValueOfList) for i in range(rangeOfList)]
    print('Первый случайно сгенерированный список: ', list1)
    list2 = [random.randint(0, maxValueOfList) for k in range(rangeOfList)]
    print('Второй случайно сгенерированный список: ', list2)
    list3 = list1 + list2
    print('Новый список, состоящий из элементов двух предыдущих списков: ', list3)
    list3.sort()
    print('Список отсортирован: ', list3)



helloFunction(int(input('Определите длину списка: ')), int(input('Максимально возможное значение элемента списка: ')))







