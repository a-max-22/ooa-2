import copy
import pickle


class General(object):
    def __init__(self):
        pass

    def copy(self, other):
        self.__dict__ = {}

        for cur_name in other.__dict__.keys():
            self.__dict__[cur_name] = copy.deepcopy(other.__dict__[cur_name])

    def clone(self):
        return copy.deepcopy(self)

    def compare(self, other):
        if type(self) != type(other):
            return False
        
        result = True
        for cur_name in self.__dict__.keys():
            cur_val = self.__dict__[cur_name]
            if cur_name not in other.__dict__:
                return False
            if isinstance(cur_val, General):
                result = cur_val.compare(other.__dict__[cur_name])
            else:
                result = ( cur_val == other.__dict__[cur_name])

        return result 


    def serialize(self):
        return pickle.dumps(self.content)

    def deserialize(self, content):
        self.content = pickle.loads(content)

    def print(self):
        for cur_name in self.__dict__.keys():
            cur_val = self.__dict__[cur_name]
            if isinstance(cur_val, General):
                cur_val.print()
            else:
                print(cur_val)

    def check_type(self, type):
        return isinstance(self.content, type)

    def get_real_type(self):
        return type(self)
    

class Any(General):
    pass


class Cookie(Any):
    def get_name(self):
        return "Cookie"

class Bread(Any):
    def get_name(self):
        return "Bread"
    

class Toast(Any):
    def get_name(self):
        return "Toast"

class Void(Cookie, Bread, TOast):
    def get_name(self):
        raise AttributeError("Void has no name")

c = Cookie()
b = Bread()
t = Toast()
v = Void()

l = [c,b,t,v]

for val in l:
    print(val.get_name())
