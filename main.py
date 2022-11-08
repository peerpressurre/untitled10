import random
def sums():
    try:
        size = int(input('size->'))
        start = int(input('start->'))
        end = int(input('end->'))

        list = []
        neg = []
        even = []
        odd = []
        summ = 0
        for i in range(size):
            list.append(random.randint(start, end))
        for i in list:
            if i < 0:
                summ += i
            if i % 2 == 0:
                even.append(i)
            if i % 2 != 0:
                odd.append(i)
        print(f'Сума відє\'мних чисел: {summ}\nСума парних чисел: {sum(even)}\nСума непарних чисел: {sum(odd)}')


    except Exception as ex:
        print(f'Error: {ex}')

sums()