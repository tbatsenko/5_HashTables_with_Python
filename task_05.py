import math

class Node(object):
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

class BasicHashTable(object):
    def __init__(self, hash_type, values):
        self.values = values

        def find_closest_prime(n):
            number = n
            prime_found = False
            for i in range(2, int(math.sqrt(number) + 2)):
                if number % i == 0:
                    break
                if i == int(math.sqrt(n) + 1):
                    prime_found = True
                    break

            if prime_found:
                return number
            number -= 1

            return number

        self.size = find_closest_prime(len(values) * 3 - 1)

        self.hash_type = hash_type

        self.hash_table = [None for el in range(self.size)]


class ChainedHash(BasicHashTable):
    def __init__(self, hash_type, values):
        super(ChainedHash, self).__init__(hash_type, values)
        self.hash = lambda key: key % self.size

    def add_element(self, num):
        curr_node = self.hash_table[self.hash(num)]
        if curr_node:
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = Node(num)
        else:
            self.hash_table[self.hash(num)] = Node(num)

    def get_element(self, num):
        curr_node = self.hash_table[self.hash(num)]
        if curr_node:
            while curr_node.next:
                if curr_node.value == num:
                    return True
                curr_node = curr_node.next
            if curr_node.value == num:
                return True
        return False


class ChainedHashMultiply(ChainedHash):
    def __init__(self, hash_type, values):
        super(ChainedHashMultiply, self).__init__(hash_type, values)
        A = 0.6180339887
        self.hash = lambda key : int(self.size*(key*A % 1))


class OpenAdressHash(BasicHashTable):
    def __init__(self, hash_type, values):
        super(OpenAdressHash, self).__init__(hash_type, values)
        self.hash = lambda key, i: (ChainedHash.hash(key) + i) % self.size

    def add_element(self, num):
        i = 0
        start_index = self.hash(num, i)
        curr_node = self.hash_table[start_index]
        if curr_node != None:
            while self.hash_table[start_index + i] != None:
                i += 1
            self.hash_table[start_index + i] = num
        else:
            self.hash_table[start_index] = num

    def get_element(self, num):
        i = 0
        start_index = self.hash(num, i)
        curr_node = self.hash_table[start_index]
        if curr_node != None:
            while self.hash_table[start_index + i] != num:
                if self.hash_table[start_index + i] == None:
                    return False
                i += 1
            return True
        else:
            return False


class OpenAdressHashSquare(OpenAdressHash):
    def __init__(self, hash_type, values):
        super(OpenAdressHashSquare, self).__init__(hash_type, values)

    def hash(key, i):
        return (ChainedHashDivision.hash(key) + i*2 + i**2 * 3) % self.size


class OpenAdressHashDouble(OpenAdressHash):
    def __init__(self, hash_type, values):
        super(OpenAdressHashDouble, self).__init__(hash_type, values)

    def hash(key, i):
        h1 = lambda x: x % self.size
        return (h1(key) + i*ChainedHashMultiply.hash(key)) % self.size


class HashTable(object):
    def __init__(self, hash_type, values):
        if hash_type == 1:
            self.current_hash_table = ChainedHash(hash_type, values)

        elif hash_type == 2:
            self.current_hash_table = ChainedHashMultiply(hash_type, values)

        elif hash_type == 3:
            self.current_hash_table = OpenAdressHash(hash_type, values)

        elif hash_type == 4:
            self.current_hash_table = OpenAdressHashSquare(hash_type, values)

        else:
            self.current_hash_table = OpenAdressHashDouble(hash_type, values)

        for el in values:
            self.current_hash_table.add_element(el)


    def get_element(self, num):
        return self.current_hash_table.get_element(num)


    def get_collisions_amount(self):
        nones_amount = 0
        for el in self.current_hash_table.hash_table:
            if el == None:
                nones_amount += 1
        return nones_amount + len(self.current_hash_table.values) - self.current_hash_table.size

    def find_sum(self, s):
        for x in range(s // 2 + 1):
            y = s - x
            if self.current_hash_table.get_element(x) and self.current_hash_table.get_element(y):
                if x + y == s:
                    return x, y
