from abc import ABC, abstractmethod
from typing import List, Union

class Value(ABC):
    @abstractmethod
    def get_value(self):
        pass

    def string(self):
        pass


class Real(Value):
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def string(self):
        return str(self._value)


class Complex(Value):
    def __init__(self, real, imaginary):
        self._real = real
        self._imaginary = imaginary

    def get_value(self):
        return (self._real, self._imaginary)

    def string(self):
        return str(self._value) + str(self._imaginary) + "*i"

# здесь применяется условное "динамическое связывание",
# когда при вызове "print" вызывается метод "string" получения строкового 
# представления заданного значения  


values = [Real(3), Real(4), Complex(5, 2)]

for value in values:
    print(value.string())
