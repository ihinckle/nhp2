class SoSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self.size = 0

    def add(self, value):
        node = SoSLinkedListNode(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size = self.size+1

    def insert_before(self, before, value):
        if not self.head:
            return None
        node = SoSLinkedListNode(value)
        if before == self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            cursor = self.head
            while cursor:
                if cursor == before:
                    cursor.prev.next = node
                    node.next = cursor
                    node.prev = cursor.prev
                    cursor.prev = node
                    break
                else:
                    cursor = cursor.next

    # def insert_after(self, after, value):
    #     if not self.head:
    #         return None
    #     node = SoSLinkedListNode(value)
    #     cursor = self.head
    #     while cursor:
    #         if cursor == after:
    #             node.next = cursor.next
    #             cursor.next = node
    #             break
    #         else:
    #             cursor = cursor.next

    def iterate(self):
        self.cursor = self.head

    def next(self):
        self.cursor = self.cursor.next

    def __str__(self):
        if not self.head:
            return str(self.head)
        cursor = self.head
        while cursor:
            print(cursor)
            cursor = cursor.next
        return ''


class SoSLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
