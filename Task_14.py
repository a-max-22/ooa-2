import copy
import pickle

class Void:
    pass

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

    @staticmethod
    def assignment_attempt(target, source):
        if not issubclass(source.get_real_type(), target.get_real_type()):
            return Void()
        return source



class Any(General):
    pass

class Integer(Any):
    def __init__(self, val):
         self.val = val

    def get_value(self):
        return self.val
    
    def add(self, another):
        return Integer(self.val + another.get_value())



class Vector(Any):
    APPEND_NIL = 0
    APPEND_OK  = 1
    APPEND_ERR = 2

    GET_NIL = 0
    GET_OK  = 1
    GET_ERR = 2

    

    def __init__(self, size = 16, item_type = Any()):
        self.size = size
        self.storage = []
        self._append_status = self.APPEND_NIL
        self._get_status = self.GET_NIL
        self._get_result = None
        self.item_type = item_type
        if not  hasattr(item_type, 'add'):
            raise AttributeError("item type %s has no add operation" % type(item_type))


    def __len__(self):
        return len(self.storage)
    
    def __str__(self):
        return str(self.storage)
    
    def capacity(self):
        return self.size
    
    def print(self):
        print('vector:')
        for elem in self.storage:
            elem.print()

    def append(self, elem):
        if not isinstance(elem, self.item_type):
            print("append err wrong type", elem)
            self._append_status = self.APPEND_ERR
            return

        if len(self) == self.size:
            self._append_status = self.APPEND_ERR
            return
        
        self._append_status = self.APPEND_OK
        self.storage.append(elem)

    def get(self, index):
        if 0 <= index < len(self):
            self._get_status = self.GET_OK
            self._get_result = self.storage[index]
            return 
        
        self._get_status = self.GET_ERR
        

    def add(self, another):
        if self.get_item_type() != another.get_item_type():
            return Void()

        if len(self) != len(another):
            return Void()
        
        sum_vect = Vector(self.size, self.item_type)
        for ind in range(0,len(self)):
            another.get(ind)
            self.get(ind)
            if another.get_get_status() != Vector.GET_OK:
                return Void()
            if self.get_get_status() != Vector.GET_OK:
                return Void()
            
            sum_vect.append(self.get_get_result().add(another.get_get_result()))
        
        return sum_vect

    def get_item_type(self):
        return self.item_type
    
    def get_get_result(self):
        return self._get_result
    
    def get_get_status(self):
        return self._get_status
    
    def get_append_status(self):
        return self._append_status
    

def fill_vector_integer(vector):
    for i in range(0, vector.capacity()):
        vector.append(Integer(i))

def gen_vector_integer(vec_size):
    v = Vector(vec_size, Integer)
    fill_vector_integer(v)
    return v

def gen_vector_vector(vectors):
    result = Vector(len(vectors), Vector)
    for vec in vectors:
        result.append(vec)
    return result

vec_size = 5
v1 = Vector(vec_size, Integer)
v2 = Vector(vec_size, Integer)
v3 = Vector(vec_size, Integer)
v4 = Vector(vec_size, Integer)

fill_vector_integer(v1)
fill_vector_integer(v2)
fill_vector_integer(v3)
fill_vector_integer(v4)

v1.add(v2).print()

V3 = gen_vector_vector(\
                        [gen_vector_vector(\
                            [gen_vector_integer(4) for i in range(0,3)]) for x in range(0,2)])
V4 = gen_vector_vector(\
                        [gen_vector_vector(\
                            [gen_vector_integer(4) for i in range(0,3)]) for x in range(0,2)])

V3.add(V4).print()