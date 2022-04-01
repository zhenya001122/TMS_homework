


def task_1():

    def add_bun(func):
        def wrapper():
            func()
            print('булка')    
        return wrapper

    def add_salad(func):
        def wrapper():
            func()
            print('салат')
        return wrapper

    def add_tomatoes(func):
        def wrapper():
            func()
            print('помидоры')
        return wrapper

    @add_tomatoes
    @add_salad
    @add_bun
    def burger(ingridient='вкусная котлета'):
        print(ingridient)

    burger()
    print('Какой вкусный бургер получился-пальчики оближешь')
# _______________________________________________
def task_2():
    def displays_name_func(func):
        def wrapper(a):
            print(f'Имя функции: {func.__name__}. Ее аргумент = {a}')
            print('Задача 2 выполнена')
            func(a)
        return wrapper

    @displays_name_func
    def func_name(a):
        print()
    func_name(5)
# __________________________________________
def task_3():
    
    def time_decorator(func):

        import time

        def wrapper_countdown(num_of_secs):
            while num_of_secs:
                m, s = divmod(num_of_secs, 60)
                min_sec_format = '{:02d}:{:02d}'.format(m, s)
                print(min_sec_format)
                time.sleep(1)
                num_of_secs -= 1
            func(num_of_secs)
        return wrapper_countdown

    @time_decorator
    def simple_func(num_of_secs):
        print('Я просто функция')
    simple_func(10)

if __name__ == '__main__':
    # task_1()
    #  task_2()
    task_3()