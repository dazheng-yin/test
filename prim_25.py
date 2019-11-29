#prim算法
class MST(object):

    def __init__(self,maps):
        self.maps=maps
        self.nodenum=self.nodenum()
        self.edgenum=self.edgenum()


    def nodenum(self):
        #返回图的节点数
        return len(self.maps)

    def edgenum(self):
        #返回边的数量
        count=0

        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j]>0 and self.maps[i][j]<9999:
                    count+=1

        return count

    def prim(self):
        #prim算法关键步骤
        mts=[]
        if self.nodenum==0 and self.edgenum<self.nodenum-1:
            return mts

        sNode=[0] #已选结点
        cNode=[i for i in range(1,self.nodenum)] #候选结点

        while len(cNode)>0:
            start,end,minweight=0,0,9999

            for i in sNode:
                for j in cNode:
                    if self.maps[i][j]<minweight:
                        minweight=self.maps[i][j]
                        start=i
                        end=j

            mts.append([start,end,minweight])
            sNode.append(end)
            cNode.remove(end)

        return mts


if __name__=="__main__":
    #邻接表
    max_weight=9999
    row0=[0,7,max_weight,max_weight,max_weight,5]
    row1=[7,0,9,max_weight,3,max_weight]
    row2=[max_weight,9,0,6,max_weight,max_weight]
    row3=[max_weight,max_weight,6,0,8,10]
    row4=[max_weight,3,max_weight,8,0,4]
    row5=[5,max_weight,max_weight,10,4,0]
    graph=[row0,row1,row2,row3,row4,row5]

    mstText=MST(graph)
    print("最小生成树的prim算法：")
    print(mstText.prim())














