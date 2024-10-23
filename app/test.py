import time


# Храним выбранные кнопки
# сет используется т.к. нужно хранить укикальные кнопки т.е. без повторений
selected_buttons = set()

# Храним фотографии в медиагруппе на уровне модуля
# ключ - integer номер группы
# значение - list - список с объектами InputMedia
media_groups = {} # dict 


# def - define - ключевое слово для функций
# async def - ключевое слово для описания асихронных функций
# await - async wait - мы ожидаем что на этой строчке будет долгоая операция которую ноужно будет ждать
#                       соответственно, можно будет передать исполнение другим потокам



def our_print(*args, **kwargs):
    for el in args:
        print(el)
    
    for key, val in kwargs.items():
        print('key =', key, 'val', val)


our_print('5', '2', '3', goo=5, b=5, c=4)

# декоратор - функция, которая принимает функцию, и подменяет её
def time_it(other):

    # *args  (как tuple) -    принимает серию аргументов (любого типа)
    # **kwargs (как dict) -  принимает серию именованных аргументов
    def wrapper(*args, **kwargs):
        time_start = time.time()

        ret = other(*args, **kwargs)

        print("Function took", time.time() - time_start)
        return ret
    
    return wrapper


@time_it
def count():
    t = 0
    for i in range(10000):
        t += i
        print(100) 
    return t

count()



# -----------------------------------------------------

# Сет - множество (оно хранит только уникальные значения)
buttons = set()
t = [1, 1, 2, 3]
t = set(t)

print('set=', set(t))
for el in t:
    print(el)


# Dict - словарь (мап) - набор пар ключ-значение
# ключи - только неизменяемые
# значения - любые
my_dict = {
    'a': 10,
    'Вася': 4.5,
    19438381: 3000,
    (104.10202, 304.93202, 42.139303): 5
}

t = [4, 4.5, 'foo', dict()]      # список, он же изменяемый контейнер
print(t)    # 4

#      {[4]: 'foo'}
t.append(5)
print(t)    # 4, 5

tpl = (3, 4, 5)     # - tuple кортеж - неизменяемый список




# ----------

# придумать примеры использования всех базовых типов 
# написать пару функций (и примеры функций с args и kwargs)
# все что интересно из файлика - попробуй написать и запустить сам


# --------
# Компилируется - проходит все проверки (типов, синтаксиса и тд.) -> исполняемый файл


# Интерпретируется - построчно код переводится в байт-код и выполняется построчно

# переменные, функции и тд. - с маленькой буквы с _
# классы - CamelCase - без _

# Модификаторы доступа файлов
# 'w' - перезапись
# 'a' - добавление в существующий файл
# 'r' - чтение

def initialize_bot(token_file_path: str):
    with open(token_file_path, 'r') as file:
      return file.read()
      

def set_token(token: str, token_file_path: str):
    # file.write('...')
    with open(token_file_path, 'w') as file:
      file.write(token)

TOKEN_FILE_NAME = "token.txt"
set_token('7720308388:AAFllQjBGydz0OI9T_hnwee-nPI3nO-3rhA', TOKEN_FILE_NAME)
print(initialize_bot(TOKEN_FILE_NAME) == '7720308388:AAFllQjBGydz0OI9T_hnwee-nPI3nO-3rhA')


# for <> in <контейнер>
# for <> in range(9) - запускает код ниже 9 раз - for (i=0 ; i < 9 ; i++)
# for <> in range(0, 9, 2) - for (i=0; i<9; i+=2)
# while <любое условие>:

# isinstance(объект, предполагаемый тип) - вернет True если объект этого типа, иначе False
# перевод из типа в тип осуществляется с помощью <название типа>(то что нужно перевести в новый тип)
# 
# 


try:    # код в блоке ниже - потенциально выведет ошибку
    t = '5a' 
    print(type(t[0]))
    t = int('5a') # t - число
except ValueError:
    print('Не смогли перевести')

t = [1, 2, 3] 
t = tuple(t) # стал кортежем

print(isinstance(type, object))


# ключевое слово class
class Bot:
    # у функции всех классов будут иметь self в качестве стандартного первого аргумента
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.g = 101


    def foo(self):
        print(self.a, self.b)
    
b = Bot(100, 99)
b.foo()


"""
map = {}    # словарь

map['key'] = {'value1', 'value2'}

values = map['key']


l = [1, 2, 3]
print(l[0])

"""

# --------------------------

# попытаться написать какие-то простые классы
# зайти в исходный код aiogram и посмотреть как там устроены некоторые классы
# старое дз - попробовать (поработать с ними) все стандартные классы и написать функции с их использованиями (и с *args, **kwarg)


# Пример

my_dict = {
    "a": 10,
    "b": 15
}

def print_dict(d):
    for key, value in d.items():
        print('key=', key, 'value=', value)

print_dict(my_dict)