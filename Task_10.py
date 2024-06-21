# в Python нет встроенного механизма запрета переопределения методов класса
# достичь такого поведения можно используя метаклассы (код взят из stackoverflow)
# В данном случае при создании класса если атрибут находится в списке запрещенных к переопределению
# будет выдаваться соответствующее исключение

def protect(*protected):
    class Protect(type):
        has_base = False
        def __new__(meta, name, bases, attrs):
            if meta.has_base:
                for attribute in attrs:
                    if attribute in protected:
                        raise AttributeError('Overriding of attribute "%s" not allowed.'%attribute)
            meta.has_base = True
            new_class = super().__new__(meta, name, bases, attrs)
            return new_class
    return Protect


class Base(metaclass=protect("protected_method")):
    def protected_method(self):
        pass

class Derived(Base):
    def protected_method(self):
        pass

# отработает корректно 
c = Base()

# исключение AttributeError 
c = Derived()
