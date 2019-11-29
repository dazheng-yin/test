#最小生成树
class MST(object):
    #最小生成树

    def __init__(self,maps):
        self.maps=maps
        self.nodenum=self.get_nodenum()
        self.edgenum=self.get_edgenum()


    def get_nodenum(self):
        #获得图的节点数
        return len(self.maps)

    def get_edgenum(self):
        #获得边的数量
        count=0
        for i in range(self.nodenum):
            for j in range(i):
                if maps[i][j]>0 and maps[i][i]<9999:
                    count+=1

        return count/2

    #kruskal算法最小生成树
    def kruskal(self):

        mts=[]
        if self.nodenum<=0 or self.edgenum<self.nodenum-1:
            return mts                            #若所给图为空或为非联通图则返回空树

        edge_list = []                            # 初始化边列表
        for i in range(self.nodenum):             # 循环头节点
            for j in range(i + 1, self.nodenum):  # 循环尾节点
                if self.maps[i][j] < 9999:
                    edge_list.append([i, j, self.maps[i][j]])

        edge_list.sort(key=lambda a: a[2])
        group = [[i] for i in range(self.nodenum)]

        for edge in edge_list:                    # 遍历边列表
            for i in range(self.nodenum):
                if edge[0] in group[i]:
                    m = i
                if edge[1] in group[i]:
                    n = i
            if m != n:
                mts.append(edge)
                group[m] = group[m] + group[n]
                group[n] = []
        return mts


max_value = 9999
row0 = [0, 7, max_value, max_value, max_value, 5]
row1 = [7, 0, 9, max_value, 3, max_value]
row2 = [max_value, 9, 0, 6, max_value, max_value]
row3 = [max_value, max_value, 6, 0, 8, 10]
row4 = [max_value, 3, max_value, 8, 0, 4]
row5 = [5, max_value, max_value, 10, 4, 0]
maps = [row0, row1, row2, row3, row4, row5]		#邻接矩阵图

graph = MST(maps)

print('邻接矩阵为\n%s' % graph.maps)
print('节点数为%d，边数为%d。\n' % (graph.nodenum, graph.edgenum))

print('------最小生成树kruskal算法------')
print(graph.kruskal())




