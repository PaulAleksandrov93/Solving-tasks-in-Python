

#ChatbotGPT
# def create_darts_board(side):
#     board = [[0] * side for _ in range(side)]
#     for i in range(side):
#         for j in range(side):
#             min_distance = min(i, j, side - i - 1, side - j - 1)
#             board[i][j] = min_distance + 1
#     return board

# # Считываем сторону игрового поля
# side = int(input())

# # Создаем игровое поле
# board = create_darts_board(side)

# # Выводим игровое поле
# for row in board:
#     print(*row)

#===

#ChatbotGPT

# def is_valid_sequence(sequence):
#     stack = []

#     for char in sequence:
#         if char == '(':
#             stack.append(char)
#         elif char == ')':
#             if not stack or stack.pop() != '(':
#                 return False

#     return len(stack) == 0

# # Считываем скобочную последовательность
# sequence = input()

# # Проверяем правильность последовательности и выводим результат
# print(is_valid_sequence(sequence))

#===

# def inversions(sequence):
#     # Рекурсивная функция для сортировки с подсчетом инверсий
#     def merge_sort(sequence):
#         if len(sequence) <= 1:
#             return sequence, 0
        
#         # Разделение последовательности пополам
#         mid = len(sequence) // 2
#         left_half, inversions_left = merge_sort(sequence[:mid])
#         right_half, inversions_right = merge_sort(sequence[mid:])
        
#         # Слияние отсортированных половин с подсчетом инверсий
#         merged, inversions = merge(left_half, right_half)
#         inversions += inversions_left + inversions_right
        
#         return merged, inversions
    
#     # Функция для слияния двух отсортированных последовательностей с подсчетом инверсий
#     def merge(left, right):
#         merged = []
#         inversions = 0
#         i, j = 0, 0
        
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 merged.append(left[i])
#                 i += 1
#             else:
#                 merged.append(right[j])
#                 j += 1
#                 inversions += len(left) - i
                
#         merged.extend(left[i:])
#         merged.extend(right[j:])
        
#         return merged, inversions
    
#     # Вызов рекурсивной функции merge_sort()
#     _, inversions_count = merge_sort(sequence)
#     return inversions_count

#===

# import sys
# data = [p.strip() for p in sys.stdin.readlines()]
# # print(len(data))
# # print(len(set(data)))
# print(data)
# print(len(data)-len(set(data)))

#===

# class ElectricCar:
#     engine_type = 'electric motor'


# car = ElectricCar()

# car.color = 'black'

# print('engine_type' in ElectricCar.__dict__)
# print('color' in ElectricCar.__dict__)

#===

# class ElectricCar:
#     pass


# car = ElectricCar()

# car.color = 'yellow'
# car.owner = 'Gvido'

# print(car.alarm_system)

#===

# class ElectricCar:
#     pass


# car = ElectricCar()

# car.color = 'black'
# car.mileage = 100

# print(car.color)
# print(car.mileage)

# car.color = 'yellow'
# car.mileage += 200

# print(car.color)
# print(car.mileage)

#===

# class ElectricCar:
#     engine_type = 'electric motor'


# car = ElectricCar()

# print(ElectricCar.engine_type)
# print(car.engine_type)

#===

# class ElectricCar:
#     pass


# car = ElectricCar()

# car.color = 'yellow'
# car.owner = 'Gvido'

# print(car.__dict__)

#===

# class ElectricCar:
#     engine_type = None


# car1 = ElectricCar()
# car2 = ElectricCar()

# ElectricCar.engine_type = 'electric motor'

# print(car1.engine_type)
# print(car2.engine_type)

#===

# class PiggyBank():
#     pass

# money_box = PiggyBank()

#===

# class PiggyBank():
#     pass

# money_box1 = PiggyBank()
# money_box2 = PiggyBank()

# money_box1.coins = 10

# money_box2.coins = 15
# money_box2.color = 'pink'

#===

# class PiggyBank():
#     content = 'coins'
#     alternate_name = 'penny bank'

# money_box = PiggyBank()
# print(money_box.content)

#===

# class ElectricCar:
#     engine_type = 'electric motor'


# car = ElectricCar()

# car.color = 'black'

# print(getattr(car, 'color'))
# print(getattr(car, 'engine_type'))

#===

# class ElectricCar:
#     pass


# car = ElectricCar()

# print(getattr(car, 'owner'))

#===

# class ElectricCar:
#     pass


# car = ElectricCar()

# setattr(car, 'color', 'yellow')

# print(car.color)
# print(car.__dict__)

#===

# class ElectricCar:
#     engine_type = 'electric motor'


# car = ElectricCar()

# car.color = 'black'

# print(hasattr(car, 'color'))
# print(hasattr(car, 'engine_type'))

#===

# class ElectricCar:
#     pass


# car = ElectricCar()

# car.color = 'black'

# delattr(car, 'color')

# print(getattr(car, 'color', None))
# print(car.__dict__)

#===

# class ElectricCar:
#     engine_type = 'electric motor'


# car = ElectricCar()

# delattr(car, 'engine_type')

# print(getattr(car, 'engine_type', None))

#===

# class ElectricCar:
#     def __init__(self):
#         print('Вызов метода __init__()')


# car1 = ElectricCar()
# car2 = ElectricCar()
# car3 = ElectricCar()

#===

# class Gun():
#     def shoot(self):
#         print('pif')

#===

# class User():
#     def __init__(self, name):
#         self.name = name
#         self.friends = 0

#     def add_friends(self, n):
#         self.friends += n

# user = User('Paul')
# user.add_friends(3)
# print(user.friends)

#===

# class House:
#     def __init__(self, color, rooms):
#         self.color = color
#         self.rooms = rooms

#     def paint(self, new_color):
#         self.color = new_color
    
#     def add_rooms(self, n):
#         self.rooms += n
        
# house = House('white', 4)

# print(house.color)
# print(house.rooms)

#===

# import math
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
#         self.diameter = radius * 2
#         self.area = math.pi * radius**2
# circle = Circle(1)
# print(circle.radius)

#===

# class Bee():
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     def move_up(self, n):
#         self.y += n

#     def move_down(self, n):
#         self.y -= n    
    
#     def move_right(self, n):
#         self.x += n

#     def move_left(self, n):
#         self.x -= n
    
# bee = Bee()

# bee.move_up(1)
# bee.move_right(1)
# bee.move_down(1)
# bee.move_left(1)

# print(bee.x, bee.y)

#===

# class Gun():
#     def __init__(self):
#         self.shot = 0
#     def shoot(self):
#         if self.shot == 0:
#             print('pif')
#             self.shot = 1
#         else:
#             print('paf')
#             self.shot = 0
    

# gun = Gun()

# gun.shoot()
# gun.shoot()
# gun.shoot()
# gun.shoot()

#===

# class Gun():
#     def __init__(self):
#         self.shot = 0
#         self.count = 0
#     def shoot(self):
#         self.count += 1
#         if self.shot == 0:
#             print('pif')
#             self.shot = 1
#         else:
#             print('paf')
#             self.shot = 0
#     def shots_count(self):
#         return self.count
#     def shots_reset(self):
#         self.count = 0

# gun = Gun()

# print(gun.shots_count())
# gun.shoot()
# print(gun.shots_count())
# gun.shoot()
# print(gun.shots_count())

#===

# class Scales():
#     def __init__(self):
#         self.mass_l = 0
#         self.mass_r = 0
#     def add_right(self, m_right):
#         self.mass_r += m_right
#     def add_left(self, m_left):
#         self.mass_l += m_left
#     def get_result(self):
#         if self.mass_r == self.mass_l:
#             return 'Весы в равновесии'
#         elif self.mass_l > self.mass_r:
#             return 'Левая чаша тяжелее'
#         else:
#             return 'Правая чаша тяжелее'

# scales = Scales()

# scales.add_right(1)
# scales.add_left(2)

# print(scales.get_result())

#===

# import math
# class Vector():
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def abs(self):
#         return math.sqrt(self.x**2 + self.y**2)
    
# vector = Vector(3, 4)

# print(vector.x, vector.y)
# print(vector.abs())

#===

# class Numbers():
#     def __init__(self):
#         self.numbers = []
#         self.even_numbers = []
#         self.odd_numbers = []

#     def add_number(self, number):
#         self.numbers.append(number)
    
#     def get_even(self):
#         self.even_numbers = []
#         for num in self.numbers:
#             if num % 2 == 0:
#                 self.even_numbers.append(num)
        
#         return self.even_numbers
    
#     def get_odd(self):
#         self.odd_numbers = []
#         for num in self.numbers:
#             if num % 2 != 0:
#                 self.odd_numbers.append(num)
        
#         return self.odd_numbers

                
        
# numbers = Numbers()

# numbers.add_number(1)
# numbers.add_number(2)
# numbers.add_number(3)
# numbers.add_number(4)

# even = numbers.get_even()
# odd = numbers.get_odd()
# print(numbers.get_even())
# print(numbers.get_odd())

# even.append(None)
# odd.append(None)
# print(numbers.get_even())
# print(numbers.get_odd())

#===

# class TextHandler():
#     def __init__(self):
#         self.kitwords = []
#         self.shortes = []
#         self.longest = []
    
#     def add_words(self, text):
#         self.text = text.split() 
#         for word in self.text:
#             self.kitwords.append(word)
        
#         return self.kitwords

#     def get_shortest_words(self):
#         if len(self.kitwords) != 0:
#             self.min_len = min([len(word) for word in self.kitwords])
#             self.shortes = [word for word in self.kitwords if len(word) == self.min_len]
#             return self.shortes
#         else:
#             return self.shortes

#     def get_longest_words(self):
#         if len(self.kitwords) != 0:
#             self.max_len = max([len(word) for word in self.kitwords])
#             self.longest = [word for word in self.kitwords if len(word) == self.max_len]
#             return self.longest
#         else:
#             return self.longest

# texthandler = TextHandler()

# texthandler.add_words('The world will hold my trial for your sins')
# texthandler.add_words('Never meant to see the sky, never meant to live')

# print(texthandler.get_shortest_words())
# print(texthandler.get_longest_words())

#===

# class Todo():
#     def __init__(self):
#         self.things = []
#         self.do_by_priority = []
#         self.low_priority = 0
#         self.d_low_priority = []
#         self.high_priority = 0
#         self.d_high_priority = []
    
#     def add(self, do, n):
        
#         self.things.append((do, n))

#     def get_by_priority(self, n):
#         # self.do_by_priority = list(map(lambda x: x[0] if x[1] == n else None, self.things))
#         self.do_by_priority =  [x[0] for x in self.things if x[1] == n]

#         return self.do_by_priority

#     def get_low_priority(self):
#         if self.things:
#             self.low_priority = min([d[1] for d in self.things])
#             for d in self.things:
#                 if d[1] == self.low_priority:
#                     self.d_low_priority.append(d[0])
#             return self.d_low_priority
#         else:
#             return self.d_low_priority

#     def get_high_priority(self):
#         if self.things:
#             self.high_priority = max([d[1] for d in self.things])
#             for d in self.things:
#                 if d[1] == self.high_priority:
#                     self.d_high_priority.append(d[0])
#             return self.d_high_priority
#         else:
#             return self.d_high_priority
    
    
# todo = Todo()

# todos = [
#     'Выбрать хостинг для своего сайта',
#     'Записаться к стоматологу',
#     'Записаться на курсы английского',
#     'Навести порядок на кухне',
#     'Подготовить одежду к лету',
#     'Подготовиться к выступлению в понедельние',
#     'Помыть машину',
#     'Пропылесосить ковры',
#     'Свозить Кемаля к ветеринару',
#     'Сходить в парикмахерскую',
#     'Посетить выставку камней'
# ]

# priorities = [4, 1, 2, 5, 2, 5, 5, 3, 3, 3, 4]
# for t, p in zip(todos, priorities):
#     todo.add(t, p)

# print(todo.get_by_priority(3))
# print(todo.get_low_priority())
# print(todo.get_high_priority())

#===

# class Postman():
#     def __init__(self):
#         self.delivery_data = []

#     def add_delivery(self, street, house, apartment):
#         self.delivery_data.append((street, house, apartment))

#     def get_houses_for_street(self, street):
#         # houses = [x[1] for x in self.delivery_data if x[0] == street and x[1]]
#         houses = []
#         for h in self.delivery_data:
#             if h[0] == street:
#                 if h[1] not in houses:
#                     houses.append(h[1])

#         return houses
#     def get_flats_for_house(self, street, house):
#         # flats = [x[2] for x in self.delivery_data if x[0] == street and x[1] == house]
#         flats = []
#         for f in self.delivery_data:
#             if f[0] == street and f[1] == house:
#                 if f[2] not in flats:
#                     flats.append(f[2])
#         return flats


# postman = Postman()

# delivery_data = [('Тульская', 149, 35), ('Запорожская', 19, 26), ('Сосновая', 33, 17), ('Высотная', 91, 44),
#                  ('Шишкина', 143, 8), ('Иванова', 60, 38), ('Веселая', 115, 19), ('Учительская', 37, 70),
#                  ('М.Горького', 167, 57), ('Северная', 128, 44), ('Железнодорожная', 121, 28), ('Пригородная', 39, 2),
#                  ('Одесская', 176, 34), ('Высоцкого', 100, 24), ('Цветочная', 168, 49), ('Павлова', 35, 62),
#                  ('Шолохова', 177, 8), ('Баумана', 27, 96), ('Димитрова', 170, 37), ('Папанина', 85, 59),
#                  ('40 лет Победы', 167, 56), ('Весенняя', 165, 63), ('Дарвина', 77, 39), ('Лунная', 200, 79),
#                  ('Иванова', 104, 20), ('Комсомольская', 38, 74), ('Дарвина', 149, 44), ('Льва Толстого', 174, 85),
#                  ('Победы', 64, 45), ('Новоселов', 128, 22)]

# for delivery in delivery_data:
#     postman.add_delivery(*delivery)

# print(postman.get_houses_for_street('Дарвина'))
# print(postman.get_flats_for_house('Новоселов', 128))

#===

# class Wordplay():


#     def __init__(self, words=[]):
#         if words:
#             self.words = list(words)
#         else:
#             self.words = []

#     def add_word(self, word):
#         if word not in self.words:
#             self.words.append(word)
    
#     def words_with_length(self, n):
#         n_words = [word for word in self.words if len(word) == n]
#         return n_words
    
#     def only(self, *args):
#         letters = ''
#         for c in args:
#             letters += c
#         only_words = []
#         for word in self.words:
#             count = 0
#             for c in word:
#                 if c in letters:
#                     count += 1
#                 if count == len(word):
#                     only_words.append(word)
#         return only_words
        
#     def avoid(self, *args):
#         letters = ''
#         for c in args:
#             letters += c
#         avoid_words = []
#         for word in self.words:
#             count = 0
#             for c in word:
#                 if c not in letters:
#                     count += 1
#                 if count == len(word):
#                     avoid_words.append(word)
#         return avoid_words



# wordz = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
# wordplay = Wordplay(wordz)

# wordz.extend(['Гуев', 'Харисов', 'Светкин'])
# print(wordz)
# print(wordplay.words)

# ===ДОПИЛИТЬ РЕШЕНИЕ, Разобраться с цветом фигуры


# import numpy as np
# class Knight():

#     def __init__(self, horizontal, vertical, color):
#         self.horizontal = horizontal
#         self.vertical = vertical
#         self.color = color

#     def get_char(self):
#         return 'N'
    
#     def can_move(self, h, v):
#         move = (h, v)     
#         matrix = [['.']*8 for _ in range(8)]
#         hor = 'abcdefgh'
#         vert = '87654321'
#         y = '87654321'.index(str(self.vertical))
#         x = 'abcdefgh'.index(self.horizontal)
#         matrix[x][y] = 'N'
#         moves = []
#         for i in range(len(matrix)):
#             for j in range(len(matrix)):
#                 if (x - i) ** 2 + (y - j) ** 2 == 5:
#                         moves.append((hor[i], j))
#         if move in moves:
#             return True
#         else:
#             return False

#     def move_to(self, h, v):
#         move = (h, v)     
#         matrix = [['.']*8 for _ in range(8)]
#         hor = 'abcdefgh'
#         vert = '87654321'
#         y = '87654321'.index(str(self.vertical))
#         x = 'abcdefgh'.index(self.horizontal)
#         matrix[x][y] = 'N'
#         moves = []
#         for i in range(len(matrix)):
#             for j in range(len(matrix)):
#                 if (x - i) ** 2 + (y - j) ** 2 == 5:
#                         moves.append((hor[i], j))
#         if move in moves:
#             self.horizontal = h
#             self.vertical = v
#             return True
#         else:
#             return False     

#     def draw_board(self):
        
#         def print_matrix(matrix, n, width=1):
#             for r in range(n):
#                 for c in range(n):
#                     print(str(matrix[r][c]).ljust(width), end=' ')
#                 print()

#         matrix = [['.']*8 for _ in range(8)]
#         y = '87654321'.index(str(self.vertical))
#         x = 'abcdefgh'.index(self.horizontal)

#         matrix[x][y] = 'N'

#         for i in range(len(matrix)):
#             for j in range(len(matrix)):
#                 if (x - i) ** 2 + (y - j) ** 2 == 5:
#                         matrix[i][j] = '*'

#         res = [c.tolist() for c in np.transpose(matrix)]
#         return print_matrix(res, 8)


# knight = Knight('e', 5, 'black')

# knight.draw_board()
# knight.move_to('d', 3)
# print()
# knight.draw_board()

# ===

# import math
# class Circle():
#     def __init__(self, radius):
#         self._radius = radius
#         self._diameter = 2 * radius
#         self._area = math.pi * radius**2
    
#     def get_radius(self):
#         return self._radius
#     def get_diameter(self):
#         return self._diameter
#     def get_area(self):
#         return self._area

# ===

# class BankAccount():

#     def __init__(self, balance=0):
#         self._balance = balance
    
#     def get_balance(self):
#         return self._balance
    
#     def deposit(self, amount):
#         self._balance += amount
    
#     def withdraw(self, amount):
#         if amount > self._balance:
#             raise ValueError('На счете недостаточно средств')
#         self._balance -= amount
        
#     def transfer(self, account, amount):
#         if amount > self._balance:
#             raise ValueError('На счете недостаточно средств')
#         self._balance -= amount
#         account.deposit(amount)
    

# account = BankAccount()

# print(account.get_balance())
# account.deposit(100)
# print(account.get_balance())
# account.withdraw(50)
# print(account.get_balance())

# ===

# class User():

#     def __init__(self, name, age):
#         if name == '' or not isinstance(name, str) or not name.isalpha():
#             raise ValueError('Некорректное имя')
#         self._name = name
#         d = [i for i in range(0, 111)]
#         if type(age) != int or age not in d:
#             raise ValueError('Некорректный возраст')
#         self._age = age

#     def get_name(self):
#         return self._name
    
#     def set_name(self, new_name):
#         if new_name == '' or not isinstance(new_name, str) or not new_name.isalpha():
#             raise ValueError('Некорректное имя')
#         self._name = new_name
    
#     def get_age(self):
#         return self._age
    
#     def set_age(self, new_age):
#         d = [i for i in range(0, 111)]
#         if type(new_age) != int or new_age not in d:
#             raise ValueError('Некорректный возраст')
#         self._age = new_age
    

# user = User('Гвидо', 67)

# user.set_name('Тимур')
# user.set_age(30)

# print(user.get_name())
# print(user.get_age())

# ===

# class Rectangle():

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def get_perimeter(self):
#         return self.length * 2 + self.width * 2 
    
#     def get_area(self):
#         return self.length * self.width
    
#     perimeter = property(get_perimeter)
#     area = property(get_area)


# rectangle = Rectangle(4, 5)

# print(rectangle.length)
# print(rectangle.width)
# print(rectangle.perimeter)
# print(rectangle.area)

# ===

# class HourClock():
    
#     def __init__(self, hours):
#         h = [i for i in range(1, 13)]
#         if hours not in h:
#             raise ValueError('Некорректное время')
#         self._hours = hours

#     def get_hours(self):
#         return self._hours
    
#     def set_hours(self, hours):
#         d = [i for i in range(1, 13)]
#         if hours not in d:
#             raise ValueError('Некорректное время')
#         self._hours = hours
       
#     hours = property(get_hours, set_hours)


# try:
#     HourClock('pizza time 🕷')
# except ValueError as e:
#     print(e)

# ===

# class Person():

#     def __init__(self, name, surname):
#         self._name = name
#         self._surname = surname

#     def get_name(self):
#         return self._name
    
#     def set_name(self, name):
#         self._name = name
    
#     def get_surname(self):
#         return self._surname
    
#     def set_surname(self, surname):
#         self._surname = surname

#     def get_fullname(self):
#         return self._name + ' ' + self._surname
    
#     def set_fullanme(self, fullname):
#         self._name, self._surname = fullname.split()

#     name = property(get_name, set_name)
#     surname = property(get_surname, set_surname)
#     fullname = property(get_fullname, set_fullanme)


# person = Person('Джон', 'Маккарти')

# person.fullname = 'Алан Тьюринг'
# print(person.name)
# print(person.surname)

# ===

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
    
#     @property    
#     def fullname(self):
#         return self.name + ' ' + self.surname
    
#     @fullname.setter
#     def fullname(self, fullname):
#         self.name, self.surname = fullname.split()


# person = Person('Mike', 'Pondsmith')

# person.name = 'Troy'
# print(person.fullname)

# ===

# def hash_function(password):
#         hash_value = 0
#         for char, index in zip(password, range(len(password))):
#             hash_value += ord(char) * index
#         return hash_value % 10**9


# class Account():
    
#     def __init__(self, login, password):
#         self._login = login
#         self._password = password
    
#     @property
#     def login(self):
#         return self._login
#     @login.setter
#     def login(self, login):
#         raise AttributeError('Изменение логина невозможно')
    
#     @property
#     def password(self):
#         return hash_function(self._password)
    
#     @password.setter
#     def password(self, password):
#         self._password = password


# account = Account('timyr-guev', 'lovebeegeek')
# try:
#     account.login = 'timyrik30'
# except AttributeError as e:
#     print(e)

# ===

# import functools, json


# def jsonify(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         f = func(*args, **kwargs)
#         return json.dumps(f)
#     return wrapper    

# @jsonify
# def make_user(id, live, options):
#     return {'id': id, 'live': live, 'options': options}
    

# print(make_user(4, False, None))

# ===

# import sys
# v = sys.stdin.readlines()
# data = list(map(lambda x:x.strip().split(', '), v))
# coordinates = []
# for e in data: 
#   lst = []
#   for i in range(len(e)):
#     if i % 2 == 0:
#       lst.append(e[i][1:])
#     else:
#       lst.append(e[i][:-1])
#   coordinates.append(lst)
# for e in coordinates:
#     if -90 <= float(e[0]) <= 90 and -180 <= float(e[1]) <= 180:
#       print(True)
#     else:
#       print(False)

# ===

# def quantify(iterable, predicate):
#     data = filter(predicate, iterable)
#     return len(list(data))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(quantify(numbers, lambda x: x > 1))

# ===

# import calendar
# from datetime import datetime

# year = int(input())
# month = int(input())
# mnth = calendar.monthcalendar(year, month)
# counter = 0
# for week in mnth:
#     if week[3] != 0:
#         counter += 1
#     if counter >= 4:
#         day = week[3]
#         break
# print(datetime(year, month, day).strftime("%d.%m.%Y"))

# ===

# def is_integer(string):
#     try:
#         int(string)
#         return True
#     except:
#         return False

# ===

# def is_decimal(string):
#     try:
#         try:
#             int(string)
#             return True
#         except:
#             float(string)
#             return True
#     except:
#         return False


# print(is_decimal('.-95'))

# ===

# def intersperse(iterable, delimeter):
#     if isinstance(iterable, str):
#         seq = [l for l in iterable]
#     else:
#         seq = list(iterable)
#     for i in seq:
#         yield i
#         if seq.index(i) != len(seq)-1:
#             yield delimeter


# inter = intersperse('beegeek', '!')
# print(next(inter))
# print(next(inter))
# print(*inter)

# ===

# def annual_return(start, percent, years):
#     for _ in range(years):
#         start += start/100*percent
#         yield start

# for value in annual_return(120000, 10, 3):
#     print(round(value))

# ===

# def pluck(data: dict, path: str, default=None):
#     if '.' in path:
#         p = path.split('.')
#     else: 
#         if path in data:
#             return data[path]
#         else: 
#             return default
#     while len(p) > 0:
#         try:
#             # value = data.get(p[0])
#             value = data[p[0]]
#             if isinstance(value, dict):
#                 data = value
#             else:
#                 return value
#             del p[0]
#         except KeyError:
#             return default
#     return data
        

# d = {'firstname': 'Тимур', 'lastname': 'Гуев', 'birthdate': {'day': 10, 'month': 'October', 'year': 1993},
#      'address': {'streetaddress': 'Часовая 25, кв. 127',
#                  'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'},
#                  'postalcode': '125315'}}

# ===

# def recviz(fn):
#     def wrapped(*args, **kwargs):
#         arg_str = ""
#         for i, arg in enumerate(args):
#             if i > 0:
#                 arg_str += ", "
#             arg_str += str(arg)

#         for kw, val in kwargs.items():
#             if arg_str:
#                 arg_str += ", "
#             arg_str += kw + "=" + str(val)

#         print(f"-> {fn.__name__}({arg_str})")
#         res = fn(*args, **kwargs)
#         print("<-", res)

#         return res

#     return wrapped

# @recviz
# def add(a, b, c, d, e):
#     return (a + b + c) * (d + e)

# add('a', b='b', c='c', d=3, e=True)


# ===

# Решить!!
# def recviz(fn):
#     def wrapped(*args, **kwargs):
#         arg_str = ""
#         for i, arg in enumerate(args):
#             if i > 0:
#                 arg_str += ", "
#             arg_str += str(arg)

#         for kw, val in kwargs.items():
#             if arg_str:
#                 arg_str += ", "
#             arg_str += kw + "=" + str(val)

#         print(f"-> {fn.__name__}({arg_str})")
#         res = fn(*args, **kwargs)
#         print("<-", res)

#         return res

#     return wrapped

# @recviz

# def add(a, b, c, d, e):
#     return (a + b + c) * (d + e)

# add('a', b='b', c='c', d=3, e=True)

# ===

# from math import sqrt


# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#         self._d = 0
    
#     @property
#     def a(self):
#         return self._a
    
#     @a.setter
#     def a(self, a):
#         self._a = a
    
#     @property
#     def b(self):
#         return self._b
    
#     @b.setter
#     def b(self, b):
#         self._b = b
    
#     @property
#     def c(self):
#         return self._c
    
#     @c.setter
#     def c(self, c):
#         self._c = c
       
#     @property
#     def x1(self):
#         self._d = self._b**2 - 4 * self._a * self._c
#         if self._d < 0:
#             return None
#         else:
#             x1 = (-self._b - sqrt(self._d))/(2 * self._a)
#             return x1

#     @property
#     def x2(self):
#         self._d = self._b**2 - 4 * self._a * self._c
#         if self._d < 0:
#             return None
#         else:
#             x2 = (-self._b + sqrt(self._d))/(2 * self._a)
#             return x2
        
#     @property
#     def view(self):
#         m1 = '+'
#         m2 = '+'
#         if self._b < 0:
#             m1 = '-'
#         if self._c < 0:
#             m2 = '-'

#         return f'{self._a}x^2 {m1} {abs(self._b)}x {m2} {abs(self._c)}'
    
#     @property
#     def coefficients(self):
#         return (self._a, self._b, self._c)
    
#     @coefficients.setter
#     def coefficients(self, data):
#         self._a = data[0]
#         self._b = data[1]
#         self._c = data[2]

        
# polynom = QuadraticPolynomial(1, 2, -3)

# polynom.coefficients = (5, 3, 1)
# print(polynom.x1)
# print(polynom.x2)
# print(polynom.view)

# ===

# class Color:

#     def __init__(self, hexcode):
#         self._hexcode = hexcode
    
#     @property
#     def r(self):
#         return int(self._hexcode[:2], 16)
    
#     @property
#     def g(self):
#         return int(self._hexcode[2:4], 16)
    
#     @property
#     def b(self):
#         return int(self._hexcode[4:], 16)

#     @property
#     def hexcode(self):
#         return self._hexcode
    
#     @hexcode.setter
#     def hexcode(self, hexcode):
#         self._hexcode = hexcode
        

# color = Color('0000FF')

# color.hexcode = 'A782E3'
# print(color.hexcode)
# print(color.r)
# print(color.g)
# print(color.b)

# ===

# class ElectricCar:
#     def __init__(self, color):
#         if not ElectricCar.is_valid(color):
#             raise ValueError
#         self._color = color

#     @staticmethod
#     def is_valid(data):
#         return isinstance(data, str) and data.isalpha()


# car = ElectricCar('black')

# print(ElectricCar.is_valid(car, 'yellow'))

# ===

# class Circle:
    
#     def __init__(self, radius):
#         self.radius = radius
    
#     def radius(self):
#         return self.radius
    
#     def radius(self, radius):
#         self.radius = radius

#     @classmethod
#     def from_diameter(cls, diameter):
#         return cls(diameter/2)


# circle = Circle.from_diameter(10)

# print(circle.radius)

# ===

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def length(self):
#         return self.length
    
#     def width(self):
#         return self.width
    
#     @classmethod
#     def square(cls, side):
#         return cls(side, side)


# rectangle = Rectangle.square(5)

# print(rectangle.length)
# print(rectangle.width)

# ===

# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
        
#     def a(self):
#         return self.a

#     def b(self):
#         return self.b
    
#     def c(self):
#         return self.c
    
#     @classmethod
#     def from_iterable(cls, iterobj):
#         return cls(iterobj[0], iterobj[1], iterobj[2])
    
#     @classmethod
#     def from_str(cls, strobj):
#         if '.' in strobj:
#             lst = list(map(lambda x: float(x), strobj.split()))
#         else:
#             lst = list(map(lambda x: float(x), strobj.split()))
#         return cls(lst[0], lst[1], lst[2])


# polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

# print(polynom.a)
# print(polynom.b)
# print(polynom.c)
# print(polynom.a + polynom.b + polynom.c)

# ===

# class Pet:
#     pet_list = []
    
#     def __init__(self, name):
#         self.name = name
#         Pet.pet_list.append(self)
        
#     @classmethod
#     def first_pet(cls):
#         if cls.pet_list:
#             return cls.pet_list[0]
#         else:
#             return None
    
#     @classmethod
#     def last_pet(cls):
#         if cls.pet_list:
#             return cls.pet_list[-1]
#         else:
#             return None
    
#     @classmethod
#     def num_of_pets(cls):
#         return len(cls.pet_list)

# ===

# class StrExtension:
#     def __init__(self):
#         pass

#     @staticmethod
#     def remove_vowels(string):
#         vowels = 'aeiouyAEIOUY'
#         result = ''
#         for char in string:
#             if char not in vowels:
#                 result += char
#         return result

#     @staticmethod
#     def leave_alpha(string):
#         result = ''
#         for char in string:
#             if char.isalpha():
#                 result += char
#         return result

#     @staticmethod
#     def replace_all(string, chars, char):
#         for old_char in chars:
#             string = string.replace(old_char, char)
#         return string

# ===

# class CaseHelper:
#     def init(self):
#         pass
    
#     @staticmethod
#     def is_snake(string):
#         words = string.split('_')
#         for word in words:
#             if not word.islower():
#                 return False
#         return True
    
#     @staticmethod
#     def is_upper_camel(string):
#         if string[0].isupper():
#             return True
#         else:
#             return False
    
#     @staticmethod
#     def to_snake(string):
#         result = ''
#         for char in string:
#             if char.isupper():
#                 result += '_' + char.lower()
#             else:
#                 result += char
#         return result
    
#     @staticmethod
#     def to_upper_camel(string):
#         result = ''
#         words = string.split('_')
#         for word in words:
#             result += word.capitalize()
#         return result
        
# print(CaseHelper.is_snake('beegeek'))
# print(CaseHelper.is_snake('bee_geek'))
# print(CaseHelper.is_snake('Beegeek'))
# print(CaseHelper.is_snake('BeeGeek'))


# ===

# from functools import singledispatchmethod


# class ElectricCar:
#     @singledispatchmethod
#     def __init__(self, color, owner):
#         self.color = color
#         self.owner = owner
    
#     @__init__.register(list)
#     def _multiple_colors_owners(self, color, owner):
#         self.color = ', '.join(color)
#         self.owner = ', '.join(owner)


# car1 = ElectricCar('black', 'Elon')
# car2 = ElectricCar('yellow', ['Gvido', 'Hideo'])

# print(car1.color, car1.owner)
# print(car2.color, car2.owner)

# ===

# from functools import singledispatchmethod


# class ElectricCar:
#     @singledispatchmethod
#     def __init__(self, color):
#         raise ValueError

#     @__init__.register(str)
#     def _from_str(self, color):
#         self.color = color
    
#     @__init__.register(list)
#     def _from_list_tuple(self, color):
#         self.color = ', '.join(color)


# car1 = ElectricCar('yellow')
# car2 = ElectricCar(['black', 'white'])

# print(car1.color)
# print(car2.color)

# ===

# from functools import singledispatch

# class Processor:
#     @singledispatch
#     def process(data):
#         raise TypeError('Аргумент переданного типа не поддерживается')
    
#     @process.register(str)
#     def process_str(data):
#         return data.upper()
    
#     @process.register(list)
#     @staticmethod
#     def process_list(data):
#         return sorted(data)
    
#     @process.register(tuple)
#     @staticmethod
#     def process_tuple(data):
#         return tuple(sorted(data))
    
#     @process.register(int)
#     @process.register(float)
#     @staticmethod
#     def process_number(data):
#         return data * 2

# print(Processor.process(10))
# print(Processor.process(5.2))
# print(Processor.process('hello'))
# print(Processor.process((4, 3, 2, 1)))
# print(Processor.process([3, 2, 1]))

# ===

# from functools import singledispatch
# class Negator:
#     @singledispatch
#     @staticmethod
#     def neg(obj):
#         raise TypeError('Аргумент переданного типа не поддерживается')

#     @neg.register(int)
#     @neg.register(float)
#     @staticmethod
#     def _(obj):
#         return -obj

#     @neg.register(bool)
#     @staticmethod
#     def _(obj):
#         return not obj
    

# print(Negator.neg(11.0))
# print(Negator.neg(-12))
# print(Negator.neg(True))
# print(Negator.neg(False))

# ===

# from functools import singledispatch

# class Formatter:
#     @singledispatch
#     @staticmethod
#     def format(obj):
#         raise TypeError('Аргумент переданного типа не поддерживается')

#     @format.register(int)
#     @staticmethod
#     def _(obj):
#         print(f'Целое число: {obj}')

#     @format.register(float)
#     @staticmethod
#     def _(obj):
#         print(f'Вещественное число: {obj}')

#     @format.register(list)
#     @staticmethod
#     def _(obj):
#         print(f'Элементы списка: {", ".join(str(x) for x in obj)}')

#     @format.register(tuple)
#     @staticmethod
#     def _(obj):
#         print(f'Элементы кортежа: {", ".join(repr(x) for x in obj)}')

#     @format.register(dict)
#     @staticmethod
#     def _(obj):
#         pairs = [] 
#         for key, value in obj.items(): 
#             pair = (key, value) 
#             pairs.append(pair) 
#         output = ", ".join([f"({repr(pair[0])}, {repr(pair[1])})" for pair in pairs]) 
#         print(f'Пары словаря: {output}')


# Formatter.format({'Cuphead': 1, 'Mugman': 3})
# Formatter.format({1: 'one', 2: 'two'})
# Formatter.format({1: True, 0: False})

# ===

# from datetime import date 
# from functools import singledispatch

# class BirthInfo: 
#     def init(self, birth_date): 
#         self.birth_date = self.check_birth_date(birth_date)

#     @singledispatch
#     def check_birth_date(self, birth_date):
#         raise TypeError('Аргумент переданного типа не поддерживается')

#     @check_birth_date.register
#     def _(self, birth_date: date):
#         self.birth_date = birth_date

#     @check_birth_date.register
#     def _(self, birth_date: str):
#         try:
#             self.birth_date = date.fromisoformat(birth_date)
#         except ValueError:
#             raise TypeError('Аргумент переданного типа не поддерживается')

#     @check_birth_date.register
#     def _(self, birth_date: (list, tuple)):
#         if len(birth_date) != 3:
#             raise TypeError('Аргумент переданного типа не поддерживается')
#         try:
#             self.birth_date = date(*birth_date)
#         except ValueError:
#             raise TypeError('Аргумент переданного типа не поддерживается')

#     @property
#     def age(self):
#         today = date.today()
#         if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
#             return today.year - self.birth_date.year - 1
#         else:
#             return today.year - self.birth_date.year

# ===

# from datetime import date
# from functools import singledispatch


# class BirthInfo:
#     @staticmethod
#     def check_birth_date(birth_date):
#         if isinstance(birth_date, date):
#             return birth_date
#         elif isinstance(birth_date, str):
#             try:
#                 return date.fromisoformat(birth_date)
#             except ValueError:
#                 raise TypeError('Аргумент переданного типа не поддерживается')
#         elif isinstance(birth_date, (list, tuple)):
#             if len(birth_date) != 3:
#                 raise TypeError('Аргумент переданного типа не поддерживается')
#             try:
#                 return date(*birth_date)
#             except ValueError:
#                 raise TypeError('Аргумент переданного типа не поддерживается')
#         else:
#             raise TypeError('Аргумент переданного типа не поддерживается')

#     def __init__(self, birth_date):
#         self.birth_date = self.check_birth_date(birth_date)

#     @property
#     def age(self):
#         today = date.today()
#         if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
#             return today.year - self.birth_date.year - 1
#         else:
#             return today.year - self.birth_date.year


# birthinfo1 = BirthInfo('2020-09-18')
# birthinfo2 = BirthInfo(date(2010, 10, 10))
# birthinfo3 = BirthInfo([2016, 1, 1])

# print(birthinfo1.birth_date)
# print(birthinfo2.birth_date)
# print(birthinfo3.birth_date)

# class Config:
#     _instance = None
    
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.program_name = "GenerationPy"
#             cls._instance.environment = "release"
#             cls._instance.loglevel = "verbose"
#             cls._instance.version = "1.0.0"
#         return cls._instance

# config = Config()
# print(config.program_name)
# print(config.environment)
# print(config.loglevel)
# print(config.version)

# ===

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def __str__(self):
#         return f"{self.title} ({self.author}, {self.year})"

#     def __repr__(self):
#         return f"Book('{self.title}', '{self.author}', {self.year})"


# book = Book('Изучаем Python', 'Марк Лутц', 2021) 
# print(book) 
# print(repr(book))

# ===

# class Rectangle: 
#     def __init__(self, length, width): 
#         self.length = length 
#         self.width = width

#     def __str__(self):
#         return f"Rectangle({self.length}, {self.width})"

#     def __repr__(self):
#         return f"Rectangle({self.length}, {self.width})"


# rectangle = Rectangle(1, 2) 
# print(str(rectangle)) 
# print(repr(rectangle))

# ===

# class Vector: 
#     def __init__(self, x, y): 
#         self.x = x 
#         self.y = y

#     def __str__(self):
#         return f"Вектор на плоскости с координатами ({self.x}, {self.y})"

#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"

# vector = Vector(1, 2) 
# print(str(vector)) 
# print(repr(vector))

# ===

# from functools import singledispatchmethod

# class IPAddress:
#     def __init__(self, ipaddress):
#         self.ipaddress = ipaddress
        
#     def __str__(self):
#         return str(self.ipaddress)
    
#     def __repr__(self):
#         return f"IPAddress('{self.ipaddress}')"
    
#     @singledispatchmethod
#     def from_input(self, ipinput):
#         return self
    
#     @from_input.register(str)
#     def _(self, ipinput):
#         return IPAddress(ipinput)
    
#     @from_input.register(list)
#     def _(self, ipinput):
#         return IPAddress('.'.join(str(octet) for octet in ipinput))
    
#     @from_input.register(tuple)
#     def _(self, ipinput):
#         return IPAddress('.'.join(str(octet) for octet in ipinput))

# ip = IPAddress('8.8.1.1')

# print(ip.from_input(str(ip)))
# print(repr(ip))

# ip = IPAddress([1, 1, 10, 10])

# print(ip.from_input(ip))
# print(repr(ip))

# ip = IPAddress((1, 1, 11, 11))

# print(ip.from_input(ip))
# print(repr(ip))


# class IPAddress: 
#     def __init__(self, ipaddress): 
#         self.ipaddress = ipaddress

#     def __str__(self):
#         if isinstance(self.ipaddress, list) or isinstance(self.ipaddress, tuple):
#             return '.'.join(str(i) for i in self.ipaddress)
#         else:
#             return str(self.ipaddress)
    
#     def __repr__(self):
#         return "IPAddress('%s')" % self.__str__()


# ip = IPAddress([1, 1, 10, 10])

# print(str(ip))
# print(repr(ip))

# ===

# class PhoneNumber:
#     def __init__(self, phone_number):
#         self.phone_number = phone_number

#     def __str__(self):
#         phone = ''
#         formattednumber = ''
#         for digit in self.phone_number:
#             if digit.isdigit():
#                 phone += digit
#         for i in range(len(phone)):
#             if i == 0:
#                 formattednumber += '('
#             if i == 3:
#                 formattednumber += ') '
#             if i == 6:
#                 formattednumber += '-'
#             formattednumber += phone[i]
#         return formattednumber

#     def __repr__(self):
#         phone = ''
#         for digit in self.phone_number:
#             if digit.isdigit():
#                 phone += digit
#         return f"PhoneNumber('{phone}')"


# phone = PhoneNumber('918 396 3389')

# print(str(phone))
# print(repr(phone))

# ===

# class AnyClass: 
#     def __init__(self, **kwargs): 
#         for key, value in kwargs.items(): 
#             setattr(self, key, value)

#     def __str__(self):
#         attributes = ', '.join([f"{key}={repr(value)}" for key, value in self.__dict__.items()])
#         return f"AnyClass: {attributes}"

#     def __repr__(self):
#         attributes = ', '.join([f"{key}={repr(value)}" for key, value in self.__dict__.items()])
#         return f"AnyClass({attributes})"


# any = AnyClass()

# print(str(any)) 
# print(repr(any))

# cowboy = AnyClass(name='John', surname='Marston')

# print(str(cowboy)) 
# print(repr(cowboy))

# ===

# class Vector: 
#     def __init__(self, x, y): 
#         self.x = x 
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"
    
#     def __repr__(self) -> str:
#         return f"Vector({self.x}, {self.y})"

#     def __eq__(self, other):
#         if isinstance(other, Vector):
#             return self.x == other.x and self.y == other.y
#         elif isinstance(other, tuple) and len(other) == 2:
#             return self.x == other[0] and self.y == other[1]
#         else:
#             return NotImplemented

#     def __ne__(self, other):
#         if isinstance(other, Vector):
#             return not (self == other)
#         elif isinstance(other, tuple) and len(other) == 2:
#             return not (self == Vector(*other))
#         else:
#             return NotImplemented


# vector = Vector(0, 1)

# print(vector.__eq__(1))
# print(vector.__ne__(1.1))
# print(vector.__gt__(range(5)))
# print(vector.__lt__([1, 2, 3]))
# print(vector.__ge__({4, 5, 6}))
# print(vector.__le__({1: 'one'}))

# ===

# import functools


# @functools.total_ordering 
# class Word: 
#     def __init__(self, word): 
#         self.word = word

#     def __repr__(self):
#         return f"Word('{self.word}')"

#     def __str__(self):
#         return f"{self.word.capitalize()}"

#     def __eq__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) == len(other.word)
#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) < len(other.word)
#         return NotImplemented
    
# print(Word('bee') == Word('hey'))
# print(Word('bee') < Word('geek'))
# print(Word('bee') > Word('geek'))
# print(Word('bee') <= Word('geek'))
# print(Word('bee') >= Word('gee'))

# ===

# class Month:
#     def __init__(self, year, month):
#         self.year = year
#         self.month = month
        
#     def __repr__(self):
#         return f"Month({self.year}, {self.month})"
    
#     def __str__(self):
#         return f"{self.year}-{self.month}"
    
#     def __eq__(self, other):
#         if isinstance(other, Month):
#             return self.year == other.year and self.month == other.month
#         elif isinstance(other, tuple) and len(other) == 2:
#             return self.year == other[0] and self.month == other[1]
#         return NotImplemented
    
#     def __ne__(self, other):
#         if isinstance(other, Month):
#             return self.year != other.year or self.month != other.month
#         elif isinstance(other, tuple) and len(other) == 2:
#             return self.year != other[0] or self.month != other[1]
#         return NotImplemented
    
#     def __lt__(self, other):
#         if isinstance(other, Month):
#             if self.year < other.year:
#                 return True
#             elif self.year == other.year:
#                 return self.month < other.month
#             return False
#         elif isinstance(other, tuple) and len(other) == 2:
#             if self.year < other[0]:
#                 return True
#             elif self.year == other[0]:
#                 return self.month < other[1]
#             return False
#         return NotImplemented
    
#     def __gt__(self, other):
#         if isinstance(other, Month):
#             if self.year > other.year:
#                 return True
#             elif self.year == other.year:
#                 return self.month > other.month
#             return False
#         elif isinstance(other, tuple) and len(other) == 2:
#             if self.year > other[0]:
#                 return True
#             elif self.year == other[0]:
#                 return self.month > other[1]
#             return False
#         return NotImplemented
    
#     def __le__(self, other):
#         if isinstance(other, Month):
#             return self < other or self == other
#         elif isinstance(other, tuple) and len(other) == 2:
#             return self < other or self == other
#         return NotImplemented
    
#     def __ge__(self, other):
#         if isinstance(other, Month):
#             return self > other or self == other
#         elif isinstance(other, tuple) and len(other) == 2:
#             return self > other or self == other
#         return NotImplemented
    
# print(Month(1999, 12) == Month(1999, 12))
# print(Month(1999, 12) < Month(2000, 1))
# print(Month(1999, 12) > Month(2000, 1))
# print(Month(1999, 12) <= Month(1999, 12))
# print(Month(1999, 12) >= Month(2000, 1))

# ===

# class Version:
#     def __init__(self, version):
#         version_parts = version.split('.')
#         self.major = int(version_parts[0]) if len(version_parts) >= 1 else 0
#         self.minor = int(version_parts[1]) if len(version_parts) >= 2 else 0
#         self.patch = int(version_parts[2]) if len(version_parts) >= 3 else 0

#     def __str__(self):
#         return f'{self.major}.{self.minor}.{self.patch}'

#     def __repr__(self):
#         return f'Version(\'{str(self)}\')'

#     def __eq__(self, other):
#         if isinstance(other, Version):
#             return self.major == other.major and self.minor == other.minor and self.patch == other.patch
#         return NotImplemented

#     def __ne__(self, other):
#         if isinstance(other, Version):
#             return not self.__eq__(other)
#         return NotImplemented

#     def __gt__(self, other):
#         if isinstance(other, Version):
#             if self.major > other.major:
#                 return True
#             elif self.major == other.major:
#                 if self.minor > other.minor:
#                     return True
#                 elif self.minor == other.minor:
#                     return self.patch > other.patch
#             return False
#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, Version):
#             return other.__gt__(self)
#         return NotImplemented

#     def __ge__(self, other):
#         if isinstance(other, Version):
#             return self.__eq__(other) or self.__gt__(other)
#         return NotImplemented

#     def __le__(self, other):
#         if isinstance(other, Version):
#             return self.__eq__(other) or self.__lt__(other)
#         return NotImplemented

#     def __hash__(self):
#         return hash((self.major, self.minor, self.patch))

#     def __bool__(self):
#         return bool(self.major or self.minor or self.patch)

#     def __int__(self):
#         return self.major


# version = Version('25')

# print(version.__eq__(1))
# print(version.__ne__(1.1))
# print(version.__gt__(range(5)))
# print(version.__lt__([1, 2, 3]))
# print(version.__ge__({4, 5, 6}))
# print(version.__le__({1: 'one'}))

# ===

# class ReversibleString: 
#     def __init__(self, string): 
#         self.string = string

#     def __str__(self):
#         return self.string

#     def __neg__(self):
#         return ReversibleString(self.string[::-1])

# string = ReversibleString('python')

# print(string) 
# print(-string)

# ===

# class Money: 
#     def __init__(self, amount): 
#         self.amount = amount

#     def __str__(self):
#         return f'{self.amount} руб.'

#     def __pos__(self):
#         return Money(abs(self.amount))

#     def __neg__(self):
#         return Money(-abs(self.amount))

# money = Money(100) 
# print(money) 
# print(+money) 
# print(-money)

# money = Money(-100) 
# print(money) 
# print(+money) 
# print(-money)

# ===

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return f'({self.x}, {self.y})'
    
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
    
#     def __pos__(self):
#         return Vector(self.x, self.y)
    
#     def __neg__(self):
#         return Vector(-self.x, -self.y)
    
#     def __abs__(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5

# vector = Vector(3, -4)

# print(+vector)
# print(-vector)
# print(abs(vector))

# ===

# class ColoredPoint:
#     def __init__(self, x, y, color=(0, 0, 0)):
#         self.x = x
#         self.y = y
#         self.color = color

#     def __str__(self):
#         return f'({self.x}, {self.y})'

#     def __repr__(self):
#         return f'ColoredPoint({self.x}, {self.y}, {self.color})'

#     def __pos__(self):
#         return ColoredPoint(self.x, self.y, self.color)

#     def __neg__(self):
#         return ColoredPoint(-self.x, -self.y, self.color)

#     def __invert__(self):
#         inverted_color = tuple(255 - c for c in self.color)
#         return ColoredPoint(self.y, self.x, inverted_color)


# point = ColoredPoint(2, -3) 
# print(+point) 
# print(-point) 
# print(~point)

# ===

# import copy
# class Matrix: 
#     def __init__(self, rows, cols, value=0): 
#         self.rows = rows 
#         self.cols = cols 
#         self.value = value 
#         self.matrix = [[value] * cols for _ in range(rows)]

#     def get_value(self, row, col):
#         return self.matrix[row][col]

#     def set_value(self, row, col, value):
#         self.matrix[row][col] = value

#     def __str__(self):
#         return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

#     def __repr__(self):
#         return f'Matrix({self.rows}, {self.cols})'

#     def __pos__(self):
#         return Matrix(self.rows, self.cols, value=1)

#     def __neg__(self):
#         r1 = Matrix(self.rows, self.cols, self.value)
#         k1 = copy.deepcopy(self.matrix)
#         r1.matrix = [[-val for val in row] for row in k1]
#         return r1

#     def __invert__(self):
#         r1 = Matrix(self.cols, self.rows, self.value)
#         k1 = copy.deepcopy(self.matrix)
#         r1.matrix = [[k1[j][i] for j in range(self.rows)] for i in range(self.cols)]
#         return r1

#     def __round__(self, ndigits=None):
#         if ndigits is None:
#             r1 = Matrix(self.rows, self.cols, value=0)
#             k1 = copy.deepcopy(self.matrix)
#             r1.matrix = [[round(val) for val in row] for row in k1]
#             return r1
#         else:
#             r1 = Matrix(self.rows, self.cols, value=0)
#             k1 = copy.deepcopy(self.matrix)
#             r1.matrix = [[round(val, ndigits) for val in row] for row in k1]
#             return r1

# matrix = Matrix(2, 3, 1)

# print(+matrix)
# print()
# print(-matrix)

# ===

# class FoodInfo: 
#     def __init__(self, proteins, fats, carbohydrates): 
#         self.proteins = proteins 
#         self.fats = fats 
#         self.carbohydrates = carbohydrates

#     def __add__(self, other):
#         if isinstance(other, FoodInfo):
#             total_proteins = self.proteins + other.proteins
#             total_fats = self.fats + other.fats
#             total_carbohydrates = self.carbohydrates + other.carbohydrates
#             return FoodInfo(total_proteins, total_fats, total_carbohydrates)
#         else:
#             return NotImplemented

#     def __mul__(self, n):
#         if isinstance(n, int) or isinstance(n, float):
#             total_proteins = self.proteins * n
#             total_fats = self.fats * n
#             total_carbohydrates = self.carbohydrates * n
#             return FoodInfo(total_proteins, total_fats, total_carbohydrates)
#         else:
#             return NotImplemented

#     def __truediv__(self, n):
#         if isinstance(n, int) or isinstance(n, float):
#             total_proteins = self.proteins / n
#             total_fats = self.fats / n
#             total_carbohydrates = self.carbohydrates / n
#             return FoodInfo(total_proteins, total_fats, total_carbohydrates)
#         else:
#             return NotImplemented
        
#     def __floordiv__(self, n):
#         if isinstance(n, int) or isinstance(n, float):
#             total_proteins = self.proteins // n
#             total_fats = self.fats // n
#             total_carbohydrates = self.carbohydrates // n
#             return FoodInfo(total_proteins, total_fats, total_carbohydrates)
#         else:
#             return NotImplemented
    
#     def __str__(self):
#         return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"


# pfc = [(751.26, 778.77, 947.51), (597.41, 508.5, 532.96), (800.55, 617.5, 525.14), (741.99, 785.53, 664.71),
#        (525.69, 892.41, 541.41), (888.8, 802.56, 868.78), (609.65, 855.43, 949.44), (705.25, 592.28, 738.72),
#        (514.88, 617.22, 557.5), (948.62, 938.7, 817.17), (783.98, 628.32, 686.38), (894.9, 815.81, 715.19),
#        (586.79, 826.68, 637.5), (670.53, 683.69, 841.56), (583.9, 607.34, 853.35), (954.67, 950.76, 822.19),
#        (718.94, 658.12, 537.2), (556.53, 686.17, 622.61), (699.8, 872.49, 908.3), (622.3, 920.97, 801.17)]

# FoodInfo.__round__ = lambda instance: FoodInfo(
#     round(instance.proteins, 2),
#     round(instance.fats, 2),
#     round(instance.carbohydrates, 2)
# )

# food1 = FoodInfo(1000, 2000, 3000)
# for p, f, c in pfc:
#     food2 = FoodInfo(p, f, c)
#     add = food1 + food2
#     mul = food1 * p
#     truediv = food1 // c
#     print(round(add), round(mul), round(truediv))

# ===

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"

#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         else:
#             return NotImplemented

#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x - other.x, self.y - other.y)
#         else:
#             return NotImplemented

#     def __mul__(self, other):
#         if isinstance(other, (int, float)):
#             return Vector(self.x * other, self.y * other)
#         else:
#             return NotImplemented

#     def __rmul__(self, other):
#         return self.__mul__(other)

#     def __truediv__(self, other):
#         if isinstance(other, (int, float)):
#             return Vector(self.x / other, self.y / other)
#         else:
#             return NotImplemented


# a = Vector(1, 2)
# b = Vector(3, 4)

# print(a + b)
# print(a - b)
# print(b + a)
# print(b - a)

# a = Vector(3, 4)

# print(a * 2)
# print(2 * a)
# print(a / 2)

# ===

# class SuperString:
#     def __init__(self, string):
#         self.string = string
  
#     def __str__(self):
#         return f"{self.string}"
    
#     def __add__(self, other):
#         if isinstance(other, SuperString):
#             return SuperString(self.string + other.string)
#         else:
#             return NotImplemented
    
#     def __mul__(self, other):
#         if isinstance(other, int):
#             return SuperString(self.string * other)
#         else:
#             return NotImplemented
    
#     def __rmul__(self, other):
#         return self.__mul__(other)
    
#     def __truediv__(self, other):
#         if isinstance(other, int):
#             return SuperString(self.string[:len(self.string) // other])
#         else:
#             return NotImplemented
    
#     def __lshift__(self, other):
#         if other == 0:
#             return self
#         if isinstance(other, int):
#             return SuperString(self.string[:-other])
#         else:
#             return NotImplemented
    
#     def __rshift__(self, other):
#         if isinstance(other, int):
#             return SuperString(self.string[other:])
#         else:
#             return NotImplemented


# s = SuperString('beegeek')
# for i in range(9):
#     print(f'{s} << {i} =', s << i)

# ===

# class PiggyBank:
#     def __init__(self, coins):
#         self.coins = coins

#     def __repr__(self):
#         return f'PiggyBank({self.coins})'

#     def __mul__(self, other):
#         return PiggyBank(self.coins * other)

#     def __imul__(self, other):
#         self.coins *= other


# bank = PiggyBank(10)

# bank *= 5

# print(bank)

# ===

# class Time:
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes

#     def __str__(self):
#         return "{:02d}:{:02d}".format(self.hours % 24, self.minutes % 60)

#     def __add__(self, other):
#         total_minutes = self.hours * 60 + self.minutes + other.hours * 60 + other.minutes
#         new_hours = (total_minutes // 60) % 24
#         new_minutes = total_minutes % 60
#         return Time(new_hours, new_minutes)

#     def __iadd__(self, other):
#         total_minutes = self.hours * 60 + self.minutes + other.hours * 60 + other.minutes
#         self.hours = (total_minutes // 60) % 24
#         self.minutes = total_minutes % 60
#         return self

# # Sample test case
# time1 = Time(25, 20)
# time2 = Time(10, 130)

# print(time1)
# print(time2)

# ===

# class Calculator:
#     def __init__(self):
#         pass
    
#     def __call__(self, a, b, operation):
#         if operation == '+':
#             return a + b
#         elif operation == '-':
#             return a - b
#         elif operation == '*':
#             return a * b
#         elif operation == '/':
#             if b == 0:
#                 raise ValueError('Деление на ноль невозможно')
#             return a / b
#         else:
#             raise ValueError('Некорректная операция')

# # Пример использования
# calculator = Calculator()
# print(calculator(10, 5, '+'))  # 15
# print(calculator(10, 5, '-'))  # 5
# print(calculator(10, 5, '*'))  # 50
# print(calculator(10, 5, '/'))  # 2.0

# try:
#     print(calculator(10, 0, '/'))  # Вызовет исключение ValueError
# except ValueError as e:
#     print(e)  # Деление на ноль невозможно

# ===

# class RaiseTo:
#     def __init__(self, degree):
#         self.degree = degree

#     def __call__(self, x):
#         return x ** self.degree

# # Пример использования
# raise_to_two = RaiseTo(2)
# print(raise_to_two(2))  # 4
# print(raise_to_two(3))  # 9
# print(raise_to_two(4))  # 16

# raise_to_three = RaiseTo(3)
# raise_to_four = RaiseTo(4)
# print(raise_to_three(3))  # 27
# print(raise_to_four(2))  # 16

# ===

# import random

# class Dice:
#     def __init__(self, sides):
#         self.sides = sides

#     def __call__(self):
#         return random.randint(1, self.sides)
    
# kingdice = Dice(6)
# print(kingdice() in [1, 2, 3, 4, 5, 6])  # True
# print(kingdice() in [1, 2, 3, 4, 5, 6])  # True
# print(kingdice() in [7, 8, 9, 10])  # False

# ===

# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def __call__(self, x):
#         return self.a * x**2 + self.b * x + self.c

# # Пример использования
# func = QuadraticPolynomial(1, 2, 1)
# print(func(1))  # 4
# print(func(2))  # 9

# func = QuadraticPolynomial(1, 3, 4)
# print(func(1))  # 8
# print(func(2))  # 14

# ===

# class Strip:
#     def __init__(self, chars):
#         self.chars = chars

#     def __call__(self, string):
#         return string.strip(self.chars)

# # Пример использования
# strip = Strip('!? ')

# print(strip('     ?beegeek!'))  # beegeek
# print(strip('!bee?geek!'))  # bee?geek

# strip = Strip('.,+-')

# print(strip('     --++beegeek++--'))  # --++beegeek
# print(strip('-bee...geek-'))  # bee...geek
# print(strip('-+,.b-e-e-g-e-e-k-+,.'))  # b-e-e-g-e-e-k

# ===

# class Filter:
#     def __init__(self, predicate):
#         self.predicate = predicate


#     def __call__(self, iterable):
#         if self.predicate is None:
#             return list(filter(bool, iterable))
#         else:
#             return list(filter(self.predicate, iterable))
        
# leave_even = Filter(lambda x: x % 2 == 0)
# numbers = [1, 2, 3, 4, 5, 6]

# print(leave_even(numbers)) # [2, 4, 6]

# ===

# from datetime import date

# class DateFormatter:
#     def __init__(self, country_code):
#         self.country_code = country_code

#     def __call__(self, d):
#         if self.country_code == 'ru':
#             return d.strftime("%d.%m.%Y")
#         elif self.country_code == 'us':
#             return d.strftime("%m-%d-%Y")
#         elif self.country_code == 'ca':
#             return d.strftime("%Y-%m-%d")
#         elif self.country_code == 'br':
#             return d.strftime("%d/%m/%Y")
#         elif self.country_code == 'fr':
#             return d.strftime("%d.%m.%Y")
#         elif self.country_code == 'pt':
#             return d.strftime("%d-%m-%Y")

# ===

# def CountCalls(func):
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         return func(*args, **kwargs)
    
#     wrapper.calls = 0
#     return wrapper

# ===

# def CachedFunction(func):
#     cache = {}

#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]

#     wrapper.cache = cache
#     return wrapper

# ===

# class SortKey:
#     def __init__(self, *args):
#         self.attributes = args

#     def __call__(self, obj):
#         return tuple(getattr(obj, attr) for attr in self.attributes)

# ===

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def __bool__(self):
#         return self.x != 0 or self.y != 0

#     def __int__(self):
#         return int((self.x ** 2 + self.y ** 2) ** 0.5)

#     def __float__(self):
#         return float((self.x ** 2 + self.y ** 2) ** 0.5)

#     def __complex__(self):
#         return complex(self.x, self.y)

# ===

# class Temperature:
#     def __init__(self, temperature):
#         self.temperature = temperature

#     def to_fahrenheit(self):
#         return (self.temperature * 9/5) + 32

#     @classmethod
#     def from_fahrenheit(cls, fahrenheit):
#         return cls((fahrenheit - 32) * 5/9)

#     def __str__(self):
#         count = len(str(self.temperature)[str(self.temperature).index('.')+1:])
#         return f"{self.temperature:.{count}f}°C"

#     def __bool__(self):
#         return self.temperature > 0

#     def __int__(self):
#         return int(self.temperature)

#     def __float__(self):
#         return float(self.temperature)
    

# t = Temperature(5.5)

# print(t)
# print(int(t))
# print(float(t))
# print(t.to_fahrenheit())

# ===

# class RomanNumeral:
#     ROMAN_VALUES = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
#     }

#     def __init__(self, number):
#         self.number = number

#     def __str__(self):
#         return self.number

#     def __int__(self):
#         result = 0
#         previous_value = 0

#         for char in reversed(self.number):
#             current_value = self.ROMAN_VALUES[char]
#             if current_value >= previous_value:
#                 result += current_value
#             else:
#                 result -= current_value
#             previous_value = current_value

#         return result

#     def __eq__(self, other):
#         if isinstance(other, RomanNumeral):
#             return self.number == other.number
#         return NotImplemented

#     def __ne__(self, other):
#         if isinstance(other, RomanNumeral):
#             return self.number != other.number
#         return NotImplemented

#     def __gt__(self, other):
#         if isinstance(other, RomanNumeral):
#             return int(self) > int(other)
#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, RomanNumeral):
#             return int(self) < int(other)
#         return NotImplemented

#     def __ge__(self, other):
#         if isinstance(other, RomanNumeral):
#             return int(self) >= int(other)
#         return NotImplemented

#     def __le__(self, other):
#         if isinstance(other, RomanNumeral):
#             return int(self) <= int(other)
#         return NotImplemented

#     def __add__(self, other):
#         if isinstance(other, RomanNumeral):
#             result = int(self) + int(other)
#             return RomanNumeral(convert_to_roman(result))
#         return NotImplemented

#     def __sub__(self, other):
#         if isinstance(other, RomanNumeral):
#             result = int(self) - int(other)
#             return RomanNumeral(convert_to_roman(result))
#         return NotImplemented

# def convert_to_roman(number):
#     ROMAN_NUMERALS = {
#         1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
#         90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
#     }

#     result = ''
#     for value, symbol in ROMAN_NUMERALS.items():
#         while number >= value:
#             result += symbol
#             number -= value
#     return result

# ===

# class MyClass:
#     def __init__(self, attr):
#         self.attr = attr
        
#     def __getattribute__(self, name):
#         return object.__getattribute__(self, name) + 1
    
#     def __getattr__(self, name):
#         return 0


# obj = MyClass(1)

# print(obj.attribute)

# ===

# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, value):
#         self.__name = value.title()

#     @property
#     def total(self):
#         return self.price * self.quantity

# ===

# class Logger:
#     def __setattr__(self, name, value):
#         if hasattr(self, name):
#             old_value = getattr(self, name)
#             print(f"Изменение значения атрибута {name} на {value}")
#             if old_value != value:
#                 super().__setattr__(name, value)
#         else:
#             print(f"Изменение значения атрибута {name} на {value}")
#             super().__setattr__(name, value)

#     def __delattr__(self, name):
#         print(f"Удаление атрибута {name}")
#         super().__delattr__(name)

# ===

# from typing import Any

# class Ord:
#     def __getattribute__(self, __name: str) -> Any:
#         return ord(__name)
    
# obj = Ord()

# print(obj.a)
# print(obj.b)    

# ===

# class DefaultObject:
#     def __init__(self, default=None, **kwargs):
#         self.default = default
#         self.__dict__.update(kwargs)

#     def __getattr__(self, name):
#         return self.default

# ===

# class NonNegativeObject:
#     def __init__(self, **kwargs):
#         for name, value in kwargs.items():
#             if isinstance(value, (int, float)):
#                 setattr(self, name, abs(value))
#             else:
#                 setattr(self, name, value)

# ===

# class ProtectedObject:
#     def __init__(self, **kwargs):
#         object.__setattr__(self, "__dict__", kwargs)

#     def __getattribute__(self, name):
#         if name.startswith("_"):
#             raise AttributeError("Доступ к защищенному атрибуту невозможен")
#         return object.__getattribute__(self, name)

#     def __setattr__(self, name, value):
#         if name.startswith("_"):
#             raise AttributeError("Доступ к защищенному атрибуту невозможен")
#         object.__setattr__(self, name, value)

#     def __delattr__(self, name):
#         if name.startswith("_"):
#             raise AttributeError("Доступ к защищенному атрибуту невозможен")
#         object.__delattr__(self, name)


# user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

# try:
#     user.__dict__['attr'] = 1
# except AttributeError as e:
#     print(e)

# ===

# def hash_function(obj):
#     obj_str = str(obj)
#     length = len(obj_str)
#     sum1 = 0
#     sum2 = 0

#     for i in range(length // 2):
#         sum1 += ord(obj_str[i]) * ord(obj_str[length - i - 1])

#     for i, char in enumerate(obj_str):
#         if length % 2 == 1 and i == length // 2:
#             sum2 += ord(char)
#         else:
#             sum2 += ord(char) * (i + 1 if i % 2 == 0 else -i)

#     result = (sum1 * sum2) % 123456791
#     return result

# print(hash_function(12345))

# ===

# class Cat:
#     def __init__(self, name):
#         self.name = name
        
#     def __eq__(self, other):
#         if isinstance(other, Cat):
#             return self.name == other.name
#         return NotImplemented
    
#     def __hash__(self):
#         return hash(self.name)


# cat1 = Cat('Кемаль')
# cat2 = Cat('Кемаль')

# print(cat1 == cat2)
# print(hash(cat1) == hash(cat2))

# ===

# class ColoredPoint:
#     def __init__(self, x, y, color):
#         self._x = x
#         self._y = y
#         self._color = color

#     @property
#     def x(self):
#         return self._x

#     @property
#     def y(self):
#         return self._y

#     @property
#     def color(self):
#         return self._color

#     def __eq__(self, other):
#         if isinstance(other, ColoredPoint):
#             return self._x == other._x and self._y == other._y and self._color == other._color
#         return NotImplemented

#     def __ne__(self, other):
#         if isinstance(other, ColoredPoint):
#             return not self.__eq__(other)
#         return NotImplemented

#     def __hash__(self):
#         return hash((self._x, self._y, self._color))

#     def __repr__(self):
#         return f"ColoredPoint({self._x}, {self._y}, '{self._color}')"

# ===

# iters = [enumerate('beegeek'), [1, 2, 3, 4, 5], 'beegeek', range(10), map(str.upper, 'beegeek'), (1, 2, 3, 4, 5), filter(None, '11010111'), {'bee': 1, 'geek': 2}, {1, 2, 3, 4, 5}, zip('bee', 'geek')]

# res = [i for i, n in enumerate(iters, start=1) if '__next__' in dir(n)]
# print(*res, sep='\n')

# ===

# class Point: 
#     def __init__(self, x, y, z): 
#         self.x = x 
#         self.y = y 
#         self.z = z

#     def __str__(self):
#         return f"Point({self.x}, {self.y}, {self.z})"

#     def __repr__(self):
#         return f"Point({self.x}, {self.y}, {self.z})"

#     def __iter__(self):
#         yield self.x
#         yield self.y
#         yield self.z


# # TEST_1:
# point = Point(1, 2, 3)

# print(list(point))

# # TEST_2:
# point = Point(1, 2, 3)
# x, y, z = point

# print(x, y, z)

# # TEST_3:
# points = [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]
# print(points)

# ===

# class DevelopmentTeam:
#     def __init__(self):
#         self.juniors = []
#         self.seniors = []

#     def add_junior(self, *developers):
#         self.juniors.extend(developers)

#     def add_senior(self, *developers):
#         self.seniors.extend(developers)

#     def __iter__(self):
#         for junior in self.juniors:
#             yield junior, 'junior'
#         for senior in self.seniors:
#             yield senior, 'senior'


# beegeek = DevelopmentTeam()

# beegeek.add_junior('Timur')
# beegeek.add_junior('Arthur', 'Valery')
# beegeek.add_senior('Gvido')
# print(*beegeek, sep='\n')

# ===

# class AttrsIterator:
#     def __init__(self, obj):
#         self.obj = obj
#         self.attrs = list(obj.__dict__.items())
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.attrs):
#             raise StopIteration
#         attr = self.attrs[self.index]
#         self.index += 1
#         return attr

# class User:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
        
# user = User('Debbie', 'Harry', 77)
# attrsiterator = AttrsIterator(user)

# print(*attrsiterator)

# ===  

# class SkipIterator:
#     def __init__(self, iterable, n):
#         self.iterable = list(iterable)
#         self.n = n
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         try:
#             result = self.iterable[self.index]
#             self.index += self.n + 1
#             return result
#         except IndexError:
#             raise StopIteration
        

# skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

# print(*skipiterator)

# ===

# import random

# class RandomLooper:
#     def __init__(self, *iterables):
#         self.iterables = iterables
#         self.flatten_iterable = []
#         self.generate_flatten_iterable()

#     def generate_flatten_iterable(self):
#         for iterable in self.iterables:
#             self.flatten_iterable.extend(iterable)
#         random.shuffle(self.flatten_iterable)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if not self.flatten_iterable:
#             raise StopIteration
#         return self.flatten_iterable.pop()

# ===

# from copy import copy


# class Peekable:
#     def __init__(self, iterable):
#         self.iterable = iter(iterable)

#     def peek(self, default=Ellipsis):
#         iterable = copy(self.iterable)
#         item = next(iterable, Ellipsis)
#         if item is Ellipsis and default is Ellipsis:
#             raise StopIteration
#         if item is Ellipsis:
#             return default
#         return item

#     def __iter__(self):
#         return self

#     def __next__(self):
#         item = next(self.iterable, Ellipsis)
#         if item is Ellipsis:
#             raise StopIteration
#         return item
            

# # TEST_1:
# iterator = Peekable('beegeek')

# print(next(iterator))
# print(next(iterator))
# print(*iterator)

# # TEST_2:
# iterator = Peekable('Python')

# print(next(iterator))
# print(iterator.peek())
# print(iterator.peek())
# print(next(iterator))
# print(iterator.peek())
# print(iterator.peek())

# # TEST_3:
# iterator = Peekable('Python')

# print(*iterator)
# print(iterator.peek(None))

# # TEST_4:
# iterator = Peekable(iter([]))

# try:
#     iterator.peek()
# except StopIteration:
#     print('Пустой итератор')

# try:
#     next(iterator)
# except StopIteration:
#     print('Пустой итератор')

# ===

# class LoopTracker:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.iterator = iter(iterable)
#         self._accesses = 0
#         self._empty_accesses = 0
#         self._last = None

#     @property
#     def accesses(self):
#         return self._accesses

#     @property
#     def empty_accesses(self):
#         return self._empty_accesses

#     @property
#     def first(self):
#         try:
#             return next(iter(self.iterable))
#         except StopIteration:
#             raise AttributeError("Исходный итерируемый объект пуст")

#     @property
#     def last(self):
#         if self._last is None:
#             raise AttributeError("Последнего элемента нет")
#         return self._last

#     def is_empty(self):
#         return self._accesses == 0 and self._empty_accesses > 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         try:
#             value = next(self.iterator)
#             self._accesses += 1
#             self._last = value
#             return value
#         except StopIteration:
#             self._empty_accesses += 1
#             raise

# loop_tracker = LoopTracker([1, 2, 3])

# print(loop_tracker.accesses)
# next(loop_tracker)
# next(loop_tracker)
# print(loop_tracker.accesses)

# ===

# class ForgivingIndexer:
#     def __init__(self, sequence):
#         self.sequence = sequence

#     def __getitem__(self, index):
#         return self.sequence[int(index)]
    
#     def __len__(self):
#         return len(self.sequence)


# words = ForgivingIndexer(['beegeek', 'pygen', 'stepik', 'python'])

# print(len(words[1.9]))

# ===

# import copy


# class SequenceZip:
#     def __init__(self, *sequences):
#         self.sequences = copy.deepcopy(sequences)

#     def __len__(self):
#         if not self.sequences:
#             return 0
#         return min(len(seq) for seq in self.sequences)

#     def __getitem__(self, index):
#         if index < 0:
#             raise IndexError("Index must be non-negative")

#         if not self.sequences:
#             raise IndexError("Index out of range")

#         items = []
#         for seq in self.sequences:
#             if isinstance(seq, dict):
#                 items.append(tuple(seq.values())[index])
#             elif seq:
#                 items.append(seq[index])
#             else:
#                 items.append(None)
#         return tuple(items)


# data = {'bee': 'bee', 'geek': 'geek'}

# sequencezip = SequenceZip(data)
# data['python'] = 'python'
# print(data)
# print(len(sequencezip))
# print(list(sequencezip))

# ===

# class OrderedSet:
#     def __init__(self, iterable=None):
#         self.items = []
#         self.set_items = set()
#         if iterable is not None:
#             for item in iterable:
#                 self.add(item)

#     def add(self, item):
#         if item not in self.set_items:
#             self.items.append(item)
#             self.set_items.add(item)

#     def discard(self, item):
#         if item in self.set_items:
#             self.items.remove(item)
#             self.set_items.remove(item)

#     def __len__(self):
#         return len(self.items)

#     def __iter__(self):
#         return iter(self.items)

#     def __contains__(self, item):
#         return item in self.set_items

#     def __eq__(self, other):
#         if isinstance(other, OrderedSet):
#             return self.items == other.items
#         elif isinstance(other, set):
#             return self.set_items == other
#         return NotImplemented

#     def __ne__(self, other):
#         if isinstance(other, OrderedSet):
#             return self.items != other.items
#         elif isinstance(other, set):
#             return self.set_items != other
#         return NotImplemented
    

# orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

# print(*orderedset)
# print(len(orderedset))

# ===

# class AttrDict:
#     def __init__(self, data=None):
#         self._data = dict(data) if data is not None else {}

#     def __getitem__(self, key):
#         return self._data[key]

#     def __getattr__(self, attr):
#         return self._data[attr]

#     def __setitem__(self, key, value):
#         self._data[key] = value

#     def __len__(self):
#         return len(self._data)

#     def __iter__(self):
#         return iter(self._data.keys())
    

# attrdict = AttrDict()

# attrdict['school_name'] = 'BEEGEEK'
# print(attrdict['school_name'])
# print(attrdict.school_name)

# ===

# class PermaDict:
#     def __init__(self, data=None):
#         self._data = dict(data) if data is not None else {}

#     def __getitem__(self, key):
#         return self._data[key]

#     def __setitem__(self, key, value):
#         if key in self._data:
#             raise KeyError('Изменение значения по ключу невозможно')
#         self._data[key] = value

#     def __delitem__(self, key):
#         del self._data[key]

#     def __len__(self):
#         return len(self._data)

#     def __iter__(self):
#         return iter(self._data)

#     def keys(self):
#         return self._data.keys()

#     def values(self):
#         return self._data.values()

#     def items(self):
#         return self._data.items()
    

# permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})

# print(*permadict)
# print(*permadict.keys())
# print(*permadict.values())
# print(*permadict.items())

# ===

# class HistoryDict:
#     def __init__(self, data=None):
#         self._data = {}
#         if data:
#             for key, value in data.items():
#                 self._data[key] = [value]

#     def __getitem__(self, key):
#         return self._data[key][-1]

#     def __setitem__(self, key, value):
#         if key in self._data:
#             self._data[key].append(value)
#         else:
#             self._data[key] = [value]

#     def __delitem__(self, key):
#         del self._data[key]

#     def __len__(self):
#         return len(self._data)

#     def __iter__(self):
#         return iter(self._data)

#     def keys(self):
#         return self._data.keys()

#     def values(self):
#         return (values[-1] for values in self._data.values())

#     def items(self):
#         return ((key, values[-1]) for key, values in self._data.items())

#     def history(self, key):
#         return self._data.get(key, [])

#     def all_history(self):
#         return {key: values.copy() for key, values in self._data.items()}

# ===

# class MutableString:
#     def __init__(self, string=''):
#         self._string = list(string)

#     def lower(self):
#         self._string = [char.lower() for char in self._string]

#     def upper(self):
#         self._string = [char.upper() for char in self._string]

#     def __str__(self):
#         return ''.join(self._string)

#     def __repr__(self):
#         return f"MutableString('{self}')"

#     def __len__(self):
#         return len(self._string)

#     def __iter__(self):
#         return iter(self._string)

#     def __getitem__(self, index):
#         if isinstance(index, slice):
#             return MutableString(''.join(self._string[index]))
#         return self._string[index]

#     def __setitem__(self, index, value):
#         if isinstance(index, slice):
#             start, stop, step = index.indices(len(self._string))
#             self._string[start:stop:step] = list(value)
#         else:
#             self._string[index] = value

#     def __delitem__(self, index):
#         if isinstance(index, slice):
#             start, stop, step = index.indices(len(self._string))
#             del self._string[start:stop:step]
#         else:
#             del self._string[index]

#     def __add__(self, other):
#         if isinstance(other, MutableString):
#             return MutableString(''.join(self._string + other._string))
#         elif isinstance(other, str):
#             return MutableString(''.join(self._string + list(other)))
#         else:
#             return NotImplemented
        

# mutablestring = MutableString('beegeek')

# mutablestring[-1] = 'ee'
# print(mutablestring)

# mutablestring[-2:] = 'geek'
# print(mutablestring)

# ===

# class Grouper:
#     def __init__(self, iterable, key):
#         self.groups = {}
#         self.key = key
#         for item in iterable:
#             self.add(item)

#     def add(self, item):
#         key = self.key(item)
#         if key not in self.groups:
#             self.groups[key] = []
#         self.groups[key].append(item)

#     def group_for(self, item):
#         key = self.key(item)
#         return key

#     def __len__(self):
#         return len(self.groups)

#     def __iter__(self):
#         return iter(self.groups.items())

#     def __contains__(self, item):
#         return item in self.groups
    
#     def __getitem__(self, key):
#         return self.groups.get(key, [])
    

# grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

# print(3 in grouper)
# print('bee' in grouper)

# ===


# def log_for(logfile, date_str):
#     with open(logfile, 'r', encoding='utf-8') as file:
#         lines = file.readlines()

#     filtered_lines = [line.split(' ')[1] + ' ' + line.split(' ', 2)[-1].strip() for line in lines if line.startswith(date_str)]

#     output_file = f"log_for_{date_str}.txt"
#     with open(output_file, 'w', encoding='utf-8') as file:
#         file.write('\n'.join(filtered_lines))

# ===

# class SuppressAll:
#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         return True

# ===

# class Greeter:
#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print(f"Приветствую, {self.name}!")
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         print(f"До встречи, {self.name}!")

# ===

# class Closer:
#     def __init__(self, obj):
#         self.obj = obj

#     def __enter__(self):
#         return self.obj

#     def __exit__(self, exc_type, exc_value, traceback):
#         if hasattr(self.obj, 'close') and callable(getattr(self.obj, 'close')):
#             self.obj.close()
#         else:
#             print("Незакрываемый объект")

# ===

# class ReadableTextFile:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = None

#     def __enter__(self):
#         self.file = open(self.filename, 'r', encoding='utf-8')
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.file:
#             self.file.close()

#     def __iter__(self):
#         return self

#     def __next__(self):
#         line = self.file.readline()
#         if line:
#             return line.rstrip('\n')
#         else:
#             raise StopIteration

# ===

# class Reloopable:
#     def __init__(self, file):
#         self.file = file
#         self.lines = []

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.file.close()
#         self.lines = []

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if not self.lines:
#             line = self.file.readline()
#             if not line:
#                 self.file.seek(0)
#                 raise StopIteration
#             self.lines.append(line.strip())
#         return self.lines.pop(0)

# ===

# import sys


# class UpperCaseWriter:
#     def __init__(self, stdout):
#         self.stdout = stdout

#     def write(self, text):
#         self.stdout.write(text.upper())

#     def flush(self):
#         self.stdout.flush()


# class UpperPrint:
#     def __init__(self):
#         self.old_stdout = None

#     def __enter__(self):
#         self.old_stdout = sys.stdout
#         sys.stdout = UpperCaseWriter(sys.stdout)

#     def __exit__(self, exc_type, exc_value, traceback):
#         sys.stdout = self.old_stdout

# ===

# class Suppress:
#     def __init__(self, *exception_types):
#         self.exception_types = exception_types
#         self.exception = None

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type and issubclass(exc_type, self.exception_types):
#             self.exception = exc_value
#             return True

# ===

# import time


# class AdvancedTimer:
#     def __init__(self):
#         self.last_run = None
#         self.runs = []
#         self.min = None
#         self.max = None

#     def __enter__(self):
#         self.start_time = time.time()
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         elapsed_time = time.time() - self.start_time
#         self.last_run = elapsed_time
#         self.runs.append(elapsed_time)

#         if self.min is None or elapsed_time < self.min:
#             self.min = elapsed_time

#         if self.max is None or elapsed_time > self.max:
#             self.max = elapsed_time

#         return False

# ===

# class HtmlTag:
#     INDENT = 2
#     depth = 0

#     def __init__(self, tag, inline=False):
#         self.tag = tag
#         self.depth = type(self).depth
#         self.inline = inline
#         self.end_char = '' if inline else '\n'

#     def __enter__(self):
#         print(' ' * type(self).INDENT * self.depth + f'<{self.tag}>', end=self.end_char)
#         type(self).depth += 1
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.inline:
#             print(f'</{self.tag}>')
#         else:
#             print(' ' * type(self).INDENT * self.depth + f'</{self.tag}>')
#         type(self).depth -= 1

#     def print(self, txt):
#         if self.inline:
#             print(txt, end=self.end_char)
#         else:
#             print(' ' * type(self).INDENT * (self.depth + 1) + txt, end=self.end_char)

# ===

# class TreeBuilder:
#     def __init__(self):
#         self.knots = [[]]
        
#     def __enter__(self):
#         self.knots.append([])
        
#     def __exit__(self, *args, **kwargs):
#         if self.knots[-1]:
#             self.knots[-2].append(self.knots[-1])
#         self.knots.pop()
    
#     def add(self, value):
#         self.knots[-1].append(value)
        
#     def structure(self):
#         return self.knots[-1]

# ===

# def hash_function(obj):
#     obj_str = str(obj)
#     first_step = 0
#     second_step = 0
#     for i in range(len(obj_str) // 2):
#         first_step += ord(obj_str[i]) * ord(obj_str[-i - 1])
#     if len(obj_str) % 2 != 0:
#         first_step += ord(obj_str[len(obj_str) // 2])
#     for i in range(len(obj_str)):
#         second_step += (-1) ** i * ord(obj_str[i]) * (i + 1)
#     return (first_step * second_step) % 123456791

# print(hash_function('python'))

# print(hash_function(12345))

# ===

# from contextlib import contextmanager

# @contextmanager
# def make_tag(tag):
#     print(tag)  # Вывод строки tag при входе в блок with
#     yield
#     print(tag)  # Вывод строки tag после выхода из блока with

# ===

# import sys
# from contextlib import contextmanager

# @contextmanager
# def reversed_print():
#     old_stdout = sys.stdout
#     sys.stdout = ReversedOutput(old_stdout)
#     yield
#     sys.stdout = old_stdout

# class ReversedOutput:
#     def __init__(self, stdout):
#         self.stdout = stdout

#     def write(self, text):
#         self.stdout.write(text[::-1])

#     def flush(self):
#         pass

# ===

# from contextlib import contextmanager

# @contextmanager
# def safe_open(filename, mode='r'):
#     file = None
#     try:
#         file = open(filename, mode)
#         yield file, None
#     except Exception as e:
#         yield None, e
#     finally:
#         if file:
#             file.close()

# ===

# import keyword

# class NonKeyword:
#     def __init__(self, name):
#         self.name = name

#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         try:
#             return instance.__dict__[self.name]
#         except KeyError:
#             raise AttributeError('Атрибут не найден')

#     def __set__(self, instance, value):
#         if isinstance(value, str) and value in keyword.kwlist:
#             raise ValueError('Некорректное значение')
#         instance.__dict__[self.name] = value

#     def __delete__(self, instance):
#         del instance.__dict__[self.name]

# ===

# class MaxCallsException(Exception):
#     pass

# class LimitedTakes:
#     def __init__(self, times):
#         self.times = times
#         self.count = 0
#         self.value = None

#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if self.count >= self.times:
#             raise MaxCallsException('Превышено количество доступных обращений')
#         if self.value is None:
#             raise AttributeError('Атрибут не найден')
#         self.count += 1
#         return self.value

#     def __set__(self, instance, value):
#         self.value = value

#     def __delete__(self, instance):
#         self.value = None
#         self.count = 0

# ===

# class TypeChecked:
#     def __init__(self, *types):
#         self.types = types
#         self.value = None

#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if self.value is None:
#             raise AttributeError('Атрибут не найден')
#         return self.value

#     def __set__(self, instance, value):
#         if not any(isinstance(value, t) for t in self.types):
#             raise TypeError('Некорректное значение')
#         self.value = value

#     def __delete__(self, instance):
#         self.value = None

# ===

# import random

# class RandomNumber:
#     def __init__(self, start, end, cache=False):
#         self.start = start
#         self.end = end
#         self.cache = cache
#         self.value = None

#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if self.cache and self.value is not None:
#             return self.value
#         self.value = random.randint(self.start, self.end)
#         return self.value

#     def __set__(self, instance, value):
#         raise AttributeError('Изменение невозможно')

#     def __delete__(self, instance):
#         self.value = None

# ===

# class Versioned:
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if not hasattr(instance, '_values'):
#             raise AttributeError('Атрибут не найден')
#         values = instance._values
#         if values:
#             return values[-1]
#         raise AttributeError('Атрибут не найден')

#     def __set__(self, instance, value):
#         if not hasattr(instance, '_values'):
#             instance._values = []
#         instance._values.append(value)

#     def get_version(self, instance, n):
#         if not hasattr(instance, '_values'):
#             raise AttributeError('Атрибут не найден')
#         values = instance._values
#         if 1 <= n <= len(values):
#             return values[n-1]
#         raise ValueError('Некорректный номер версии')

#     def set_version(self, instance, n):
#         if not hasattr(instance, '_values'):
#             raise AttributeError('Атрибут не найден')
#         values = instance._values
#         if 1 <= n <= len(values):
#             instance._values = values[:n]
#         else:
#             raise ValueError('Некорректный номер версии')

# ===

# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class WaterVehicle(Vehicle):
#     pass

# class AirVehicle(Vehicle):
#     pass

# class Car(LandVehicle):
#     pass

# class Motorcycle(LandVehicle):
#     pass

# class Bicycle(LandVehicle):
#     pass

# class Propeller(AirVehicle):
#     pass

# class Jet(AirVehicle):
#     pass

# ===

# class Shape:
#     pass

# class Polygon(Shape):
#     pass

# class Circle(Shape):
#     pass

# class Triangle(Polygon):
#     pass

# class Quadrilateral(Polygon):
#     pass

# class IsoscelesTriangle(Triangle):
#     pass

# class EquilateralTriangle(Triangle):
#     pass

# class Parallelogram(Quadrilateral):
#     pass

# class Rectangle(Parallelogram):
#     pass

# class Square(Rectangle):
#     pass

# ===

# class Animal:
#     def sleep(self):
#         pass

#     def eat(self):
#         pass

# class Fish(Animal):
#     def swim(self):
#         pass

# class Bird(Animal):
#     def lay_eggs(self):
#         pass

# class FlyingBird(Bird):
#     def fly(self):
#         pass

# ===

# class User:
#     def __init__(self, name):
#         self.name = name

#     def skip_ads(self):
#         return False

# class PremiumUser(User):
#     def skip_ads(self):
#         return True

# ===

# class Validator:
#     def __init__(self, obj):
#         self.obj = obj

#     def is_valid(self):
#         return None


# class NumberValidator(Validator):
#     def is_valid(self):
#         return isinstance(self.obj, (int, float))

# ===

# class Counter:
#     def __init__(self, start=0):
#         self.value = start

#     def inc(self, num=1):
#         self.value += num

#     def dec(self, num=1):
#         self.value -= num
#         if self.value < 0:
#             self.value = 0


# class NonDecCounter(Counter):
#     def dec(self, num=1):
#         pass


# class LimitedCounter(Counter):
#     def __init__(self, start=0, limit=10):
#         super().__init__(start)
#         self.limit = limit

#     def inc(self, num=1):
#         super().inc(num)
#         if self.value > self.limit:
#             self.value = self.limit

# ===

# class WeatherWarning:
#     def rain(self):
#         print("Ожидаются сильные дожди и ливни с грозой")

#     def snow(self):
#         print("Ожидается снег и усиление ветра")

#     def low_temperature(self):
#         print("Ожидается сильное понижение температуры")


# class WeatherWarningWithDate(WeatherWarning):
#     def rain(self, date):
#         print(date.strftime("%d.%m.%Y"))
#         print("Ожидаются сильные дожди и ливни с грозой")

#     def snow(self, date):
#         print(date.strftime("%d.%m.%Y"))
#         print("Ожидается снег и усиление ветра")

#     def low_temperature(self, date):
#         print(date.strftime("%d.%m.%Y"))
#         print("Ожидается сильное понижение температуры")

# ===

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def perimeter(self):
#         return self.a + self.b + self.c


# class EquilateralTriangle(Triangle):
#     def __init__(self, side):
#         super().__init__(side, side, side)

# ===

# class Counter:
#     def __init__(self, start=0):
#         self.value = start

#     def inc(self, n=1):
#         self.value += n

#     def dec(self, n=1):
#         self.value = max(self.value - n, 0)
        
# class DoubledCounter(Counter):
#     def inc(self, num=None):
#         if num is None:
#             self.value += 2
#         else:
#             self.value += 2 * num

#     def dec(self, num=None):
#         if num is None:
#             self.value -= 2
#         else:
#             self.value -= 2 * num
#         if self.value < 0:
#             self.value = 0

# ===

# class Summator:
#     def total(self, n):
#         return sum(range(1, n+1))

# class SquareSummator(Summator):
#     def total(self, n):
#         return sum(i*i for i in range(1, n+1))

# class QubeSummator(Summator):
#     def total(self, n):
#         return sum(i*i*i for i in range(1, n+1))

# class CustomSummator(Summator):
#     def __init__(self, m):
#         self.m = m
    
#     def total(self, n):
#         return sum(i**self.m for i in range(1, n+1))

# ===

# class BasicPlan:
#     can_stream = True
#     can_download = True
#     has_SD = True
#     has_HD = False
#     has_UHD = False
#     num_of_devices = 1
#     price = "8.99$"


# class SilverPlan(BasicPlan):
#     has_HD = True
#     num_of_devices = 2
#     price = "12.99$"


# class GoldPlan(BasicPlan):
#     has_HD = True
#     has_UHD = True
#     num_of_devices = 4
#     price = "15.99$"

# ===

# class UpperPrintString(str):
#     def __str__(self):
#         return super().__str__().upper()

# ===

# class LowerString(str):
#     def __new__(cls, obj=''):
#         return super().__new__(cls, str(obj).lower())

# ===

# class FuzzyString(str):
#     def __eq__(self, other):
#         if isinstance(other, str):
#             return self.lower() == other.lower()
#         return NotImplemented

#     def __ne__(self, other):
#         if isinstance(other, str):
#             return self.lower() != other.lower()
#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, str):
#             return self.lower() < other.lower()
#         return NotImplemented

#     def __gt__(self, other):
#         if isinstance(other, str):
#             return self.lower() > other.lower()
#         return NotImplemented

#     def __le__(self, other):
#         if isinstance(other, str):
#             return self.lower() <= other.lower()
#         return NotImplemented

#     def __ge__(self, other):
#         if isinstance(other, str):
#             return self.lower() >= other.lower()
#         return NotImplemented

#     def __contains__(self, item):
#         if isinstance(item, str):
#             return item.lower() in self.lower()
#         return False

# ===

# class TitledText(str):
#     def __new__(cls, content, text_title):
#         instance = super().__new__(cls, content)
#         instance.text_title = text_title
#         return instance

#     def title(self):
#         return str(self.text_title)

# ===

# class RoundedInt(int):
#     def __new__(cls, num, even=True):
#         if even:
#             rounded_num = num + 1 if num % 2 != 0 else num
#         else:
#             rounded_num = num if num % 2 != 0 else num + 1
#         return super().__new__(cls, rounded_num)

# ===

# class ModularTuple(tuple):
#     def __new__(cls, iterable=None, size=100):
#         if iterable is None:
#             iterable = []
#         return super(ModularTuple, cls).__new__(cls, (x % size for x in iterable))

# ===

# from collections import UserList

# class DefaultList(UserList):
#     def __init__(self, iterable=None, default=None):
#         super().__init__(iterable)
#         self.default = default

#     def __getitem__(self, index):
#         try:
#             return self.data[index]
#         except IndexError:
#             return self.default

# ===

# from collections import UserDict

# class TwoWayDict(UserDict):
#     def __setitem__(self, key, value):
#         self.data[key] = value
#         self.data[value] = key

# ===

# class AdvancedList(list):
#     def join(self, separator=' '):
#         return separator.join(map(str, self))

#     def map(self, func):
#         for i in range(len(self)):
#             self[i] = func(self[i])

#     def filter(self, func):
#         self[:] = [x for x in self if func(x)]

# ===

# class ValueDict(dict):
#     def key_of(self, value):
#         for key, val in self.items():
#             if val == value:
#                 return key
#         return None

#     def keys_of(self, value):
#         return [key for key, val in self.items() if val == value]

# ===

# from collections import UserDict

# class BirthdayDict(UserDict):
#     def __setitem__(self, key, value):
#         if value in self.values():
#             duplicate_keys = [k for k, v in self.items() if v == value]
#             print(f"Хей, {key}, не только ты празднуешь день рождения в этот день!")
#             for duplicate_key in duplicate_keys:
#                 del self.data[duplicate_key]
#         super().__setitem__(key, value)

#     def update(self, other=None, **kwargs):
#         if other:
#             for key, value in other.items():
#                 self[key] = value
#         if kwargs:
#             self.update(kwargs)

# ===

# from abc import ABC, abstractmethod

# class Middle(ABC):
#     def __init__(self, user_votes, expert_votes):
#         self.user_votes = user_votes
#         self.expert_votes = expert_votes

#     def get_correct_user_votes(self):
#         return [vote for vote in self.user_votes if 10 < vote < 90]

#     def get_correct_expert_votes(self):
#         return [vote for vote in self.expert_votes if 5 < vote < 95]

#     @abstractmethod
#     def get_average(self, users=True):
#         pass

# class Average(Middle):
#     def get_average(self, users=True):
#         if users:
#             votes = self.get_correct_user_votes()
#         else:
#             votes = self.get_correct_expert_votes()

#         return sum(votes) / len(votes)

# class Median(Middle):
#     def get_average(self, users=True):
#         if users:
#             votes = sorted(self.get_correct_user_votes())
#         else:
#             votes = sorted(self.get_correct_expert_votes())

#         return votes[len(votes) // 2]

# class Harmonic(Middle):
#     def get_average(self, users=True):
#         if users:
#             votes = self.get_correct_user_votes()
#         else:
#             votes = self.get_correct_expert_votes()

#         return len(votes) / sum(map(lambda vote: 1 / vote, votes))

# ===

from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, self)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    @abstractmethod
    def validate(self, value):
        pass

    def get_name(self, instance):
        for attr_name, attr_value in instance.__class__.__dict__.items():
            if attr_value is self:
                return attr_name
        raise AttributeError("Атрибут не найден")

class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Устанавливаемое значение должно быть числом")
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f"Устанавливаемое число должно быть больше или равно {self.minvalue}")
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f"Устанавливаемое число должно быть меньше или равно {self.maxvalue}")

class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Устанавливаемое значение должно быть строкой")
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть больше или равна {self.minsize}")
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}")
        if self.predicate is not None and not self.predicate(value):
            raise ValueError("Устанавливаемая строка не удовлетворяет дополнительным условиям")

class Student:
    age = Number(18, 99)

student = Student()
try:
    print(student.age)
except AttributeError as e:
    print("Атрибут не найден")