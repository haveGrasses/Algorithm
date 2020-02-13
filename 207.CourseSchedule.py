from typing import List


class Solution:
    """
    // 这个方法相当于是实现下面这个 wiki alg (https://en.wikipedia.org/wiki/Topological_sorting)

    L ← Empty list that will contain the sorted nodes
    while exists nodes without a permanent mark do
        select an unmarked node n
        visit(n)

    function visit(node n)
        if n has a permanent mark then return
        if n has a temporary mark then stop   (not a DAG)  // important
        mark n with a temporary mark
        for each node m with an edge from n to m do
            visit(m)
        remove temporary mark from n
        mark n with a permanent mark
        add n to head of L

    虽然我觉得这个实现略显复杂（尤其是在solve的dfs过程中还要判断是否有环，dfs函数是有返回值的）
    但是尝试简化的思路无果，（除了notebook里那种直接修改图的方法
    """
    def buildGraph(self, inDegree, outDict, prerequisites):
        """邻接list，只存了所有node指向的node，以及所有node的入度，不存指向node的node
        也就是存node的孩子节点，只存父亲节点的数量，并不存父亲节点到底有哪些，
        当然也可以将inDegree也改成一个dict存下父亲节点，但是没必要！
        ps. 在一个连续数组为key的情况下，可以直接用list来表示，没必要用dict，list的索引就是key
        """
        for edge in prerequisites:
            inDegree[edge[0]] += 1  # 增加该节点的入度
            outDict[edge[1]].append(edge[0])

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0 for _ in range(numCourses)]  # index是节点，value是节点的入度
        outDict = [[] for _ in range(numCourses)]  # index是节点，value是list，存的是孩子节点
        self.buildGraph(inDegree, outDict, prerequisites)
        return self.solve(outDict)

    def solve(self, outDict):
        visited = [0 for _ in range(len(outDict))]
        onStack = [0 for _ in range(len(outDict))]
        order = []
        for i in range(len(outDict)-1, -1, -1):
            # 在self.dfs调用的过程中已经在向order中添加元素了，
            # 只不过如果最后返回值是False，说明有环，order有值也没用了，直接返回一个空列表
            if not visited[i] and not self.dfs(i, outDict, visited, onStack, order):
                return []
        res = []
        while order:
            res.append(order.pop())
        return res

    def dfs(self, fromNode, outDict, visited, onStack, order):
        """ 返回值是是否能够找到order，如果有环返回的是False """
        visited[fromNode] = 1
        onStack[fromNode] = 1

        for toNode in outDict[fromNode]:
            if not visited[toNode]:
                # 对toNode进行dfs遍历+一边遍历一边check是否有环，可以减少dfs的深度
                if not self.dfs(toNode, outDict, visited, onStack, order):  # 在子节点遇到环
                    return False
            elif onStack[toNode]:  # 在当前节点遇到环
                return False

        onStack[fromNode] = 0
        order.append(fromNode)
        return True


print(Solution().findOrder(2, [[0, 1], [1, 0]]))


# class Solution:
#     """ 这是一个夭折了的solution """
#     def buildGraph(self, inDegree, outDict, prerequisites):
#         for edge in prerequisites:
#             inDegree[edge[0]] += 1  # 增加该节点的入度
#             outDict[edge[1]].append(edge[0])
#
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         inDegree = [0 for _ in range(numCourses)]  # index是节点，value是节点的入度
#         outDict = [[] for _ in range(numCourses)]  # index是节点，value是list，存的是孩子节点
#         self.buildGraph(inDegree, outDict, prerequisites)
#
#         self.visited = [0 for _ in range(len(outDict))]
#         self.tmpVisited = [0 for _ in range(len(outDict))]
#         res = []
#
#         for i in range(len(self.visited)):  # while exist unseen nodes
#             if not self.visited[i]:
#                 self.dfs(i)
#
#     def dfs(self, node):
#         pass
