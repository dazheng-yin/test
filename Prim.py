
class Graph(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()

    def get_nodenum(self):
        return len(self.maps)

    def get_edgenum(self):
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0 and self.maps[i][j] < 9999:
                    count += 1
        return count

    def prim(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
            return res
        res = []
        seleted_node = [0]
        candidate_node = [i for i in range(1, self.nodenum)]

        while len(candidate_node) > 0:
            begin, end, minweight = 0, 0, 9999
            for i in seleted_node:
                for j in candidate_node:
                    if self.maps[i][j] < minweight:
                        minweight = self.maps[i][j]
                        begin = i
                        end = j
            res.append([begin, end, minweight])
            seleted_node.append(end)
            candidate_node.remove(end)
        return res


max_value = 9999
row0 = [0, 7, max_value, max_value, max_value, 5]
row1 = [7, 0, 9, max_value, 3, max_value]
row2 = [max_value, 9, 0, 6, max_value, max_value]
row3 = [max_value, max_value, 6, 0, 8, 10]
row4 = [max_value, 3, max_value, 8, 0, 4]
row5 = [5, max_value, max_value, 10, 4, 0]
maps = [row0, row1, row2, row3, row4, row5]
graph = Graph(maps)
print('邻接矩阵为\n%s' % graph.maps)
print('节点数据为%d，边数为%d\n' % (graph.nodenum, graph.edgenum))

print('------最小生成树prim算法')
print(graph.prim())