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
from datetime import date
from functools import singledispatch


class BirthInfo:
    @staticmethod
    def check_birth_date(birth_date):
        if isinstance(birth_date, date):
            return birth_date
        elif isinstance(birth_date, str):
            try:
                return date.fromisoformat(birth_date)
            except ValueError:
                raise TypeError('Аргумент переданного типа не поддерживается')
        elif isinstance(birth_date, (list, tuple)):
            if len(birth_date) != 3:
                raise TypeError('Аргумент переданного типа не поддерживается')
            try:
                return date(*birth_date)
            except ValueError:
                raise TypeError('Аргумент переданного типа не поддерживается')
        else:
            raise TypeError('Аргумент переданного типа не поддерживается')

    def __init__(self, birth_date):
        self.birth_date = self.check_birth_date(birth_date)

    @property
    def age(self):
        today = date.today()
        if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
            return today.year - self.birth_date.year - 1
        else:
            return today.year - self.birth_date.year


birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)