import  binascii
import hashlib

# Пример наследования с конкретизацией
class Storage:
    def save(self, data):
        pass

    def load(self, data):
        pass

class FileStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, 'wb') as f:
            f.write(data)

    def load(self):
        with open(self.filename, 'rb') as f:
            return f.read()

# Пример наследования с вариацией
class HexEncodedFileStorage(FileStorage):
    def load(self):
        with open(self.filename, 'r') as f:
            return binascii.unhexlify(f.read())


# Структурное наследование
class IntegrityChecker:
    CHECK_NIL = 0
    CHECK_OK = 1
    CHECK_ERR = 2

    def __init__(self):
        self.data_hash = None
        self.check_integrity_result = self.CHECK_NIL
    
    def set_data_to_track(self, data):
        h = hashlib.new('sha256')
        h.update(data)
        self.data_hash = h.digest()

    def check_data_integrity(self, data):
        if self.data_hash is None:
            self.check_integrity_result = self.CHECK_ERR
            return 
        h = hashlib.new('sha256')
        h.update(data)
        if h.digest != self.data_hash:
            self.check_integrity_result = self.CHECK_ERR
            return
        
        self.check_integrity_result = self.CHECK_OK


    def get_check_data_integrity_result(self):
        return self.check_integrity_result
    
#прототипы методов остаются прежними, при этом мы можем дополнительно проверить целостность
#загруженных из хранилища данных вызовом IntegrityCheckingStorage.get_check_data_integrity_result() 
class IntegrityCheckingStorage(Storage, IntegrityChecker):
    def save(self, data):
        super().save(data)
        self.set_data_to_track(data)

    def load(self):
        data = super().load()
        self.check_data_integrity(data)
        return data

