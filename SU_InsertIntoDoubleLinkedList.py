class Node(object):
    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.pre = self.head
    
    def length(self):
        length = 0
        cur = self.head
        
        while cur:
            length += 1
            cur = cur.next
        
        return length
    
    def get(self, index):
        length = self.length()
        
        if length == 0:
            raise Exception('Error: Cannot get value from null LinkedList')
        
        index = index if index > 0 else length + index
        if index >= length or index < 0:
            raise Exception('Error: illegal index')
        cur = self.head.next
        while index:
            cur = cur.next
            index -= 1
        return cur
    
    def insert(self, index, value):
        """
        :param index: support both positive and negative index
        param value: insert value
        :return: None
        """
        # check 
        # 当链表为空时，插入出错，就像list一样，只有在非空的情况下才能插入
        length = self.length()
        if length == 0:
            raise Exception('Error: Null LinkedList')
        
        # 对负的index进行修正
        index = index if index >= 0 else index + length  
        
        # 判断index的合法性
        if index >= length or index < 0:
            raise Exception('Error: illegal index')
        
        cur = self.get(index)  # index位置的当前元素
        
        if cur:
            node = Node(value)
            pre_node = cur.pre
            
            pre_node.next = node
            node.pre = pre_node
            
            node.next = cur
            cur.pre = node
