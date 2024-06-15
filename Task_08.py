from typing import TypeVar, Generic, Union

# пример ковариантности: 
# класс множество DerivedClass является подмножеством BaseClass
# опредеделяя ClassesCollection через  BaseGenType, с заданной опцией covariant=True 
# мы достигаем возможности использовать производный тип DerivedClass в функции ClassesCollection
BaseGenType = TypeVar('BaseGenType', covariant=True)

class BaseClass: 
    def __init__(self, val:str):
        self.val = val

    def get_val(self):
        return 'base:' + self.val

class DerivedClass(BaseClass): 
    def get_val(self):
        return 'derived:' + self.val

class ClassesCollection(Generic[BaseGenType]):
    def __init__(self):
        self.list = []
        self.index = 0

    def add(self, val:BaseGenType):
        self.list.append(val)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        result = self.list[self.index]
        self.index += 1
        return result
        

def print_items(collection: ClassesCollection[BaseClass]): 
    for item in collection:
        print(item.get_val())

collection = ClassesCollection()
collection.add(DerivedClass('1'))
collection.add(DerivedClass('2'))
collection.add(DerivedClass('3'))

print_items(collection)



# пример контравариантности: 
# здесь в объявлении типа  BaseGenType2 задана возможность сводить 
# его к типам BaseClass и AnotherBaseClass за счет использования Union 
# в качечестве ограничения типа 
class AnotherBaseClass: 
    def __init__(self, val:str):
        self.val = val

    def get_val(self):
        return 'another base:' + self.val

class AnotherDerivedClass(AnotherBaseClass): 
    def get_val(self):
        return 'another derived:' + self.val

BaseGenType2 = TypeVar('BaseGenType2', bound = Union[BaseClass, AnotherBaseClass], covariant=True)

class AnotherClassesCollection(Generic[BaseGenType2]):
    def __init__(self):
        self.list = []
        self.index = 0

    def add(self, val:BaseGenType2):
        self.list.append(val)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        result = self.list[self.index]
        self.index += 1
        return result
        

def another_print_items(collection_1: AnotherClassesCollection[BaseClass],collection_2: AnotherClassesCollection[AnotherBaseClass]): 
    for item in collection_1:
        print(item.get_val())

    for item in collection_2:
        print(item.get_val())

collection_0 = AnotherClassesCollection()
collection_0.add(DerivedClass('1'))
collection_0.add(DerivedClass('2'))
collection_0.add(DerivedClass('3'))

collection_1 = AnotherClassesCollection()
collection_1.add(AnotherDerivedClass('1'))
collection_1.add(AnotherDerivedClass('2'))
collection_1.add(AnotherDerivedClass('3'))

another_print_items(collection_0, collection_1)