class SoSBinaryTree:
    def __init__(self):
        self.__root = None

    def insert(self, item, key):
        if not self.__root:
            self.__root = SoSNode(key, item)
        else:
            current = self.__root
            while current is not None:
                current_key = current.get_key()
                if key < current_key:
                    if not current.get('left'):
                        current |= {'left': {'key': key, 'value': item, 'left': None, 'right': None}}
                        break
                    else:
                        current = current.left
                elif key > current_key:
                    if current.right is None:
                        current.right = item
                        break
                    else:
                        current = current.right

    def get_root(self):
        if not self.__root:
            return None

        return self.__root.get_value()


class SoSNode:
    def __init__(self, key, value):
        self.__left = None
        self.__right = None
        self.__key = key
        self.__value = value

    def get_key(self):
        return self.__key

    def get_value(self):
        return self.__value

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right
