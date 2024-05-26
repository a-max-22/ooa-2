class Storage:
    def __init__(self, data):
        self.data = data

# пример наследования: базовый класс Iterator, от которого порождаются иные подклассы, 
# реализующие обход элементов Storage в обратном порядке (BackwardIterator), а также 
# реализующий фильтрацию элементов при обходе (FilteredIterator)

# пример композиции: экземпляр класса Storage является полем класса Iterator 
class Iterator:
    def __init__(self, storage):
        self.storage = storage
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.storage.data):
            raise StopIteration
        result = self.storage.data[self.index]
        self.index += 1
        return result



class BackwardIterator(Iterator):
    def __init__(self, storage):
        super().__init__(storage)
        self.index = len(self.storage.data) - 1

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        result = self.storage.data[self.index]
        self.index -= 1
        return result


class FilteredIterator(Iterator):
    def __init__(self, storage, filter_function):
        super().__init__(storage)
        self.filter_function = filter_function

    def __next__(self):
        while self.index < len(self.storage.data):
            item = self.storage.data[self.index]
            self.index += 1
            if self.filter_function(item):
                return item
        raise StopIteration


# полиморфизм: в функцию печати можно передавать разные
# типы итераторов, порожденные одним базовым классом "Iterator"
def print_items(iter:Iterator, description: str):
    print(description)
    for item in iter:
        print("%s," % item)


storage = Storage([1, 2, 3, 4, 5])

forward_iterator = Iterator(storage)
print_items(forward_iterator, "ForwardIterator")

backward_iterator = BackwardIterator(storage)
print_items(backward_iterator, "BackwardIterator")

filtered_iterator = FilteredIterator(storage, filter_function=lambda x: x % 2 == 0)
print_items(backward_iterator, "FilteredIterator")
