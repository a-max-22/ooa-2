
# вариант 1: метод, публичный в базовом классе публичен в дочернем
from typing import Any


class Base1:
    def print_hello(self):
        print("Hello!")


class Derived1(Base1):
    pass

# вариант 2: метод, приватный  в базовом классе приватен в дочернем:
# в данном случае мы применяем соглашение 
class Base2:
    def __print_hello_internal(self):
        print("Good Afternoon!")

    def print_hello(self):
        self.__print_hello_internal()


class Derived2(Base2):
    pass


# вариант 2: метод, приватный  в базовом классе приватен в дочернем:
class Base2:
    def _print_hello_internal(self):
        print("Good Afternoon!")

    def __getattribute__(self, name: str):
        if name == "_print_hello_internal":
            raise AttributeError("Attribute %s is private" % name)
        
        return object.__getattribute__(self, name)
 

class Derived2(Base2):
    pass


# вариант 3: метод, приватный  в базовом классе публичен в дочернем:
class Base3:
    def _print_hello_internal(self):
        print("Good Evening!")

    def __getattribute__(self, name: str):
        if name == "_print_hello_internal":
            raise AttributeError("Attribute %s is private" % name)
        
        return object.__getattribute__(self, name)


class Derived3(Base3):
    def __getattribute__(self, name: str):
        if name == "_print_hello_internal":
            return object.__getattribute__(self, name)


# вариант 4: метод, публичный в базовом классе приватен в дочернем:
class Base4:
    def _print_hello_internal(self):
        print("Good Night!")


class Derived4(Base4):
    def __getattribute__(self, name: str):
        if name == "_print_hello_internal":
            raise AttributeError("Attribute %s is private" % name)
        
        return object.__getattribute__(self, name)


# Примеры для случая публичных методов в наследнике и потомке : 
base1 = Base1()
derived1 = Derived1()

base1.print_hello()
derived1.print_hello()

# Примеры для случая приватных методов в наследнике и потомке : 
base2 = Base2()
derived2 = Derived2()

# исключения "Attribute error"
try:    
    base2._print_hello_internal()
except Exception as e:
    print(e)

try:    
    derived2._print_hello_internal()
except Exception as e:
    print(e)



# Примеры для случая приватного метода в базовом классе и публичного в наследнике:
base3 = Base3()
derived3 = Derived3()

# исключение "Attribute error"
try:    
    base3._print_hello_internal()
except Exception as e:
    print(e)

# всё отрабатывает нормально: 
derived3._print_hello_internal()



# Примеры для случая публичного метода в базовом классе и приватного в наследнике:
base4 = Base4()
derived4 = Derived4()

# всё отрабатывает нормально: 
base4._print_hello_internal()

# исключение "Attribute error"
try:    
    derived4._print_hello_internal()
except Exception as e:
    print(e)
