class Solution:
    """用10叉树的视角思考，用cur来记录目前移动到的节点，只要是保证先序遍历就能保证cur
     是按照字母序的顺序移动的。但不用实际地执行先序遍历。每次先考虑向右移动cur+=1跳过该节点的子树，如超了再向下移动cur*=10
     计算cur和cur+1之间的steps时，while加上每层的数量，当node1超过n时break
     """
    def calc_steps(self, node1, node2, n):
        """计算的是以node1为根的树到以node2为根的树之间隔了多少个节点
        :param node1: 沿着以初始node1为根的树的最左节点向下走
        :param node2: 沿着以初始node2为根的树的最左节点向下走，始终是node1所在的树的当前level最右节点的下一个右节点，
                      node1: 1, node2: 2; node1: 10, node2: 20; node1: 100, node2: 2000
        :param n: 上界
        """
        steps = 0
        while node1 <= n:  # <=: 当上界n与node1重合时，算一个节点数，还是要进入循环
            steps += min(node2, n + 1) - node1
            node1 *= 10
            node2 *= 10
        return steps
    
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k > 0:  # >: k表示cur还要移动多少步，未清零时都需要继续走
            steps = self.calc_steps(cur, cur + 1, n)
            if steps <= k:  # <=: steps刚好就是剩下要走的步长，就走完这个步长
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur
