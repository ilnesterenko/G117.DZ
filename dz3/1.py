
A = int(input("A: "))
B = int(input("B: "))

if A > B:
    print("Свершилось!")
elif B > A:
    print("Да ну!")
elif A == 0 & B == 0:
    print('0')
elif A == B:
    print("А если так?")
    while A == B:
        A = A + B
        print('New A:' , A)
        B = B - A
        print('New B:', B)
        if A > B:
            print("Свершилось!")
        elif B > A:
            print("Да ну!")





