"""
向双链表中指定位置插入一个元素，首先实现一个双链表，通过一个辅助的Node结构来作为双链表中的data
实现：
    - 求链表的长度
    - 打印链表
    - 向链表结尾添加元素
    - 获取指定索引的节点  -->  辅助在指定索引插入节点
    - **向指定索引插入元素**， 其余元素一次后移
"""
class Node(object):
    def __init__(self, value):
        self.val = value
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
        
        return length-2
    
    def toString(self):
        cur = self.head.next
        res = 'None'
        while cur:
            if cur.val is None:
                res += f'--> None'
            else:
                res += f'--> {cur.val.val}'
            cur = cur.next
        print(res)
    
    def get(self, index):
        length = self.length()
        
        if length == 0:
            raise Exception('Error: cannot get value from null linkedList')
        
        index = index if index >= 0 else length + index
        if index >= length or index < 0:
            raise Exception('Error: illegal index')
        cur = self.head.next
        while index:
            cur = cur.next
            index -= 1
        return cur
    
    def append(self, value):
        node = Node(value)
        pre = self.tail.pre
        
        pre.next = node
        node.pre = pre
        
        self.tail.pre = node
        node.next = self.tail
    
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
            node = Node(Node)
            node.val = Node(value)
            print('[debug]', node, node.val, node.pre, node.next)
            pre_node = cur.pre
            
            pre_node.next = node
            node.pre = pre_node
            
            node.next = cur
            cur.pre = node
