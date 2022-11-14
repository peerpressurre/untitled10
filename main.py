import random
from operator import index


def swap(min_in, max_in):
    pass


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
        mul = 1
        for i in range(size):
            list.append(random.randint(start, end))
        print(list)
        for i in list:
            if i < 0:
                summ += i
            if i % 2 == 0:
                even.append(i)
            if i % 2 != 0:
                odd.append(i)

        for i in range(3, len(list), 3):
            mul *= list[i]

        print(f'Сума відє\'мних чисел: {summ}\nСума парних чисел: {sum(even)}\nСума непарних чисел: {sum(odd)}')


        minn = list.index(min(list))
        maxx = list.index(max(list))

        mul2 = 1

        if minn > maxx:
            minn, maxx = maxx, minn

        for i in range(minn, maxx+1):
            mul2 *= list[i]

        print(f'Добуток елементів з індексами, кратними 3: {mul}')
        print(f'Добуток елементів між мінімальним та максимальним елементом: {mul2}')

        star = en = 0
        mul3 = 0
        for i in list:
            if i > 0:
                star = list.index(i)
                break
        for i in list:
            if i > 0:
                en = list.index(i)

        for i in range(star, en + 1):
            mul3 += list[i]

        print(f'Сума елементів, що знаходяться між першим та останнім додатним елементом: {mul3}')



    except Exception as ex:
        print(f'Error: {ex}')

sums()