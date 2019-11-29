#哈弗曼树
class huffman:

    class Node:
        __slots__ = 'data','left','right','weight'

        def __init__(self,data,weight):
            #初始化
            self.data=data
            self.left=None
            self.right=None
            self.weight=0

    def min_2(self,arr):
        #找出权值最小的两个值
        min2=[self.Node(None,float('inf')),self.Node(None,float('inf'))]
        temp=[]

        for i in range(len(arr)):
            if arr[i].weight<min2[0].weight:
                if min2[0].weight!=float('inf'):
                    temp.append(min2[0])

                min2[0],min2[1]=arr[i],min2[0]

            elif arr[i].weight<min2[1].weight:
                if min2[1]!=float('inf'):
                    temp.append(min2[1])

                min2[1]=arr[i]

            else:
                temp.append(arr[i])

        return min2,temp


    def make_huffman(self,source):
        #生成哈弗曼树
        min2,data=self.min_2(source)
        print(min2[0],min2[1])  #输出两个即将合并的结点

        left=min2[0]
        right=min2[1]

        sumLR=left.weight+right.weight
        father=self.Node(None,sumLR)

        father.left=left
        father.right=right

        if data==[]:
            return

        data.append(father)

        return make_huffman(data)


sourceData = [('a', 8), ('b', 5), ('c', 3), ('d', 3), ('e', 8), ('f', 6), ('g', 2), ('h', 5), ('i', 9), ('j', 5), ('k', 7), ('l', 5), ('m', 10), ('n', 9)]

huffman=huffman()
h1 =huffman.make_huffman(sourceData)



























