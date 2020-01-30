
A = int(input("A: "))
B = int(input("B: "))

while A < B:
    A = A + B
    print('Значение A:', A)
    if A < B:
         print('Пока что нет')
    else:
        print('Дождались')
        print('Финальный А:', A)








