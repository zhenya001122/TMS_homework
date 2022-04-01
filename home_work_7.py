from functools import reduce
from task_6 import lambda_filter, lambda_map


#def fff():


def lambda_map():
    """принимает список из дробных чисел
    и округляет их до целого числа.
    """
    values = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]
    result = list(map(lambda x: round(x), values))
    print(result)

def lambda_filter():
    """возвращает список из чисел больше 80"""
    scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]
    result = list(filter(lambda x: x > 80, scores))
    print(result)

def palindrom():
    """ищет слова палиндромы из списка"""
    values = ["demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP"]
    result = list(filter(lambda word: word == word[::-1], values))
    print(result)

def product_of_numbers():
    """подсчитывает произведение чисел из списка"""
    values=[1, 2, 3, 4]
    result = reduce(lambda x, y: x*y, values)
    print(result)

# def more_num():
#     """возвращает большее число из списка"""
#     values=[3, 5, 2, 4, 7, 1]
#     result = map(lambda x: , values)
#     print(result)

def count_word():
    """Подсчитsdftn количество слова "капитан" в списке"""
    sentences = ['капитан джек воробей', 'капитан дальнего плавания', 
    'ваша лодка готова, капитан'
    ]
    count = 0
    # result = filter(lambda x: count+=1 if 'капитан' in x.split() else count+=0, sentences )#разобраться
    res = reduce(lambda x, y: x+1 if y == 'капитан' else x+1, sentences, 0 )
    print(res)

if __name__ == '__main__':
#    lambda_map()
#    lambda_filter()
   palindrom()
#    product_of_numbers()
   #more_num()
#    count_word()
