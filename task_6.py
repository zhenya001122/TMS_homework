def decorator_func():
    """не могу разобраться с декораторами ((("""



#сделать lambda функцию
from functools import reduce

def lambda_map():
    """возводит число в степень"""
    L = [1, 2, 3, 4]
    print(list(map(lambda x: x**2, L)))

def lambda_reduce():
    """кумулирует числа"""
    result = reduce(lambda x, y: x*y, [4, 5], 10)
    print(result)
    # не хочет выводить в list, выводит только в int. Почему?

def lambda_filter():
    """фильтрует четные числа из списка"""
    print(list(filter(lambda x: x%2 == 0, [1, 4, 6, 8, 3])))

if __name__ == '__main__':
   #decorator_func()
   #lambda_map()
   lambda_reduce()
#    lambda_filter()