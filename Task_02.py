# пример расширения при наследовании: 
# класс Storage реализует некоторое хранилище элементов ключ-значение
# класс PersistentStorage расширяет класс-предок Storage возможностью 
# сохранения содержимого в постоянном хранилище
class Storage:
    def __init__(self):
        self.data = {}

    def add_item(self, key, value):
        self.data[key] = value

    def get_item(self, key):
        return self.data.get(key)

    def remove_item(self, key):
        if key in self.data:
            del self.data[key]


class PersistentStorage(Storage):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as f:
                data = f.read()
                if data:
                    self.data = eval(data)
        except FileNotFoundError:
            print("File not found. Initializing empty storage.")

    def save_data(self):
        with open(self.file_path, 'w') as f:
            f.write(str(self.data))

    def add_item(self, key, value):
        super().add_item(key, value)
        self.save_data()

    def remove_item(self, key):
        super().remove_item(key)
        self.save_data()

# пример специализации при наследовании:
# TreeNode - узел дерева, имеющий произвольное число потомков
# BinaryTreeNode - узел бинарного дерева, имеющий только два потомка
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

class BinaryTreeNode(TreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.left = None
        self.right = None

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node