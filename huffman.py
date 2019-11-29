#哈夫曼树
class huffmantree:
    #哈弗曼树类

    class Node:
        #结点的定义
        __slots__ = 'element','weight','left','right'

        def __init__(self,element,weight):
            self.element=element
            self.weight=weight
            self.left=left
            self.right=right

    def minTwo(self,data):
        #判断两个权值最小的结点
        min2=[Node[None,float('inf'),Node(None,float('inf'))]]
        arr=[]
        for i in range(len(data)):

            if min2[0].weight>data[i].weight:
                if min2[0].weight!=float('inf'):
                    arr.append(min2[0])

                min[0],min[1]=data[i],min[0]

            elif min[1].weight>data[i].weight:
                if min[1].weight!=float('inf'):
                    arr.append(min2[1])

                min2[1]=data[i]

            else:
                arr.append(data[i])

        return min2,arr

    def make_huffman(self,source):
        #生成哈弗曼树
        min2,arr=minTwo(source)
        print(min2[0],min[1])
        left=min2[0]
        right=min2[1]

        sumlr=min[0].weight+min[1].weight
        father=Node(None,sumlr)
        father.left=left
        father.right=right

        if data=[]:
            return

        arr.append(father)

        return make_huffman(arr)



























