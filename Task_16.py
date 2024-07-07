#Пример полимфорфного вызова метода
from typing import TypeVar, Generic, Union

class X:
    def string(self):
        return "X"
    
class Y(X):
    def string(self):
        return "Y"


def print_object_x(x:X):
    print(x.string())

x = X()
print_object_x(x)

y = Y()
print_object_x(y)


#Пример ковариантного вызова метода
T = TypeVar('T', covariant=True)

class Rational: 
    def __init__(self, nominator:int, denominator:int):
        self.nominator = nominator
        self.denominator = denominator

    def add(self, other):
        nom, denom = other.get()
        nominator =  self.nominator * denom + nom * self.denominator
        denominator =  self.denominator * denom
        return Rational(nominator, denominator)

    def get(self):
        return (self.nominator, self.denominator)
    

class Number(Rational):
    def __init__(self, val:int):
        self.nominator = val
        self.denominator = 1

    def add(self, other):
        return Number(self.get_int_val() + other.get_int_val())

    def get_int_val(self):
        return self.nominator

class Addable(Generic[T]):
    def __init__(self, val:T):
        self.val = val
    
    def add(self, other:T):
        return Addable(self.val.add(other.get()))

    def get(self):
        return self.val


def sum(a:Addable[T], b:Addable[T]):
    return a.add(b)

r1 = Addable(Rational(2,3))
r2 = Addable(Rational(3,4))

print(sum(r1,r2).get().get())

n1 = Addable(Number(1))
n2 = Addable(Number(2))

print(sum(n1,n2).get().get())

