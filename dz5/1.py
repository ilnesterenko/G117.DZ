
def watchMaker(secondsValue):

    days = secondsValue % (86400 * 30) // 86400
    hours = secondsValue % (3600 * 24) // 3600
    minutes = secondsValue % (60 * 60) // 60
    seconds = secondsValue % 60

    print(days, ':', hours, ':', minutes, ':', seconds)

watchMaker(int(input('Введите количество секунд: ')))






