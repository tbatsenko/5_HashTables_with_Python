import math

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class ChainedHashMultiplication(BasicHashTable):
    def hash(self, key):
        A = 0.6180339887
        return len(self.size*(key*A % 1)

    def __init__(self, hash_type, values):
        super().__init__(self, hash_type, values)

    def add_element(self, num):
        curr_node = self.hash_table[self.hash(num)]
        if curr_node:
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = Node(num)
        else:
            self.hash_table[self.hash(num)] = num

    def get_element(self, num):
        curr_node = self.hash_table[self.hash(num)]
        if curr_node:
            while curr_node.next:
                if curr_node.value == num:
                    return True
                curr_node = curr_node.next
        return False



class ChainedHashDivision(BasicHashTable):
    def hash(self, key):
        return key % self.size

    def __init__(self, hash_type, values):
        super().__init__(self, hash_type, values)

    def add_element(self, num):
        curr_node = self.hash_table[self.hash(num)]
        if curr_node:
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = Node(num)
        else:
            self.hash_table[self.hash(num)] = num

    def get_element(self, num):
        curr_node = self.hash_table[self.hash(num)]
        if curr_node:
            while curr_node.next:
                if curr_node.value == num:
                    return True
                curr_node = curr_node.next
        return False


class OpenAdressHashLinear(BasicHashTable):
    def __init__(self, hash_type, values):
        super().__init__(self, hash_type, values)

    def hash(key, i):
        return (ChainedHashDivision.hash(key) + i) % self.size


class OpenAdressHashSquare(BasicHashTable):
    def __init__(self, hash_type, values):
        super().__init__(self, hash_type, values)

    def hash(key, i):
        return (ChainedHashDivision.hash(key) + i*2 + i**2 * 3) % self.size


class OpenAdressHashDouble(BasicHashTable):
    super().__init__(self, hash_type, values)
        super().__init__(self, values)

    def hash(key, i):
        h1 = lambda x: x % self.size
        return (h1(key) + i*ChainedHashMultiplication.hash(key)) % self.size


class HashTable:
    def __init__(self, hash_type, values):
        self.values = values

        def find_closest_prime(n):
            number = n
            prime_found = False
            while True:
                for i in range(2, int(Math.sqrt(number) + 2)):
                    if number % i == 0:
                        break
                    if i == int(Math.sqrt() + 1:
                        prime_found = True

            if prime_found:
                return number
            number -= 1

        self.size = find_closest_prime(len(values) * 3 - 1)

        self.hash_type = hash_type

        self.hash_table = [None for el in range(self.size)]

        for num in values:
            if self.hash_type == 1:
                curr_index = ChainedHashDivision.hash(num)

            elif self.hash_type == 2:
                curr_index = ChainedHashMultiplication.hash(num)

            elif self.hash_type == 3:
                curr_index = OpenAdressHashLinear.hash(num)

            elif self.hash_type == 4:
                curr_index = OpenAdressHashSquare.hash(num)

            else:
                curr_index = OpenAdressHashDouble.hash(num)

            self.hash_table[curr_index] = num

    def get_element(self, num):
        if self.hash_type == 1:
            if self.hash_table[ChainedHashDivision.hash(num)]:
                if self.hash_table[ChainedHashDivision.hash(num)] == num:
                    return True
                else:
                    while condition:
                        pass

        elif self.hash_type == 2:
            curr_index = ChainedHashMultiplication.hash(num)

        elif self.hash_type == 3:
            curr_index = OpenAdressHashLinear.hash(num)

        elif self.hash_type == 4:
            curr_index = OpenAdressHashSquare.hash(num)

        else:
            curr_index = OpenAdressHashDouble.hash(num)






    def get_collisions_amount(self):
        nones_amount = 0
        for el in self.hash_table:
            if el == None:
                nones_amount += 1
        return nones_amount + len(self.values) - self.size

    def find_sum(s):
        for x in range(s // 2):
            y = s - x
            if
















"""
В роботі необхідно реалізувати різні типи хеш-таблиць із використанням різних хеш-функцій
для розв’язання наведеної вище задачі.
При цьому потрібно порівняти ефективність різних підходів шляхом підрахунку
кількості колізій для кожного типу хеш-функцій та хеш-таблиць.

Нижче наведений перелік типів хеш-таблиць та хеш-функцій:

1. Хеш-таблиця на основі ланцюгів (chained hash) із використанням хеш-функції за методом ділення.

2. Хеш-таблиця на основі ланцюгів (chained hash) із використанням хеш-функції за методом множення.

3. Хеш-таблиця на основі відкритої адресації (open address hash) із використанням хеш-функції за методом лінійного дослідження.

4. Хеш-таблиця на основі відкритої адресації (open address hash) із використанням хеш-функції за методом квадратичного дослідження.

5. Хеш-таблиця на основі відкритої адресації (open address hash) із використанням хеш-функції за методом подвійного хешування.

Увага!! Розмір хеш-таблиці T не повинен перевищувати потрійного розміру вхідного масиву A.

Реалізація

Ви повинні створити модуль task_05.py, в якому реалізувати клас HashTable з наступними методами:

__init__(hash_type, values) - ініціалізує хеш-таблицю.
hash_type - ціле число від 1 до 5, яке визначає тип завдання (див. перелік типів хеш-таблиць у розділі Завдання)
values - масив вхідних даних, які є цілими числами
get_collisions_amount() - повертає кількість колізій, які були отримані при ініціалізації хеш-таблиці - додаванні елементів з масиву values у конструкторі
find_sum(s) - повертає пару цілих чисел x, y, таких що x + y = s або None, якщо серед значень в таблиці не було знайдено таких два числа, що їх сума дорівнює s

    """
