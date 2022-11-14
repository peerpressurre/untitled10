import random
from operator import index


def swap(min_in, max_in):
    pass


def sums():
    try:
        size = int(input('size->'))
        start = int(input('start->'))
        end = int(input('end->'))
        nums = list()
        evens = list()
        odds = list()
        negative = list()
        positive = list()

        for i in range(size):
            nums.append(random.randint(start, end))
        print(nums)

        for i in nums:
            if i % 2 == 0:
                evens.append(i)
            if i % 2 != 0:
                odds.append(i)
            if i < 0:
                negative.append(i)
            if i > 0:
                positive.append(i)

        print(f'Even numbers: {evens}\nOdd numbers {odds}\nNegative numbers: {negative}\nPositive numbers: {positive}')




    except Exception as ex:
        print(f'Error: {ex}')

sums()