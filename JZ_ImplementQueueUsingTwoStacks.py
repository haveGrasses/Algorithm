class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, node):
        self.stack1.append(node)
        
    def pop1(self):
        """自己写的有点垃圾"""
        if self.stack2:  # 优先去2里面pop
            return self.stack2.pop()

        while self.stack1:  # 当2为空时，再把1中所有的元素都倒腾过来，然后每次pop2中的
            self.stack2.append(self.stack1.pop())
        # # 当然这里可以加个stack2是否为空的判断，不加也行
        # if not self.stack2:
        #     raise Exception('queue is empty')
        return self.stack2.pop()
    
    def pop(self):
        """更简练的pop：最终都是要去stack2里面pop的，就把return self.stack2.pop()放到最后"""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # # 当然这里可以加个stack2是否为空的判断，不加也行
        # if not self.stack2:
        #     raise Exception('queue is empty')
        return self.stack2.pop()
