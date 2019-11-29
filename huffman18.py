#哈弗曼树
class huffman:

    class Node:
        __slots__ = 'value','weight','left','right'

        def __init__(self,value,weight):
            self.value=value
            self.weight=weight
            self.left=None
            self.right=None


    def min_2(self,data):
        minTwo=[self.Node(None,float('inf')),self.Node(None,float('inf'))]
        arr=[]

        for i in range(len(data)):
            if minTwo[0].weight>data[i]:
                if minTwo[0].weight!=float('inf'):
                    arr.append(minTwo[0])

                minTwo[0],minTwo[1]=data[i],minTwo[1]

            elif data[i].weight<minTwo[1].weight:
                if minTwo[i].weight!=float('inf'):
                    arr.append(minTwo[1])
                minTwo[1]=data[i]
            else:
                arr.append(data[i])

        return minTwo,arr



    def makeHuffman(self,source):
        #生成哈弗曼树
        min2,arr=self.min_2(source)
        print(min2[1],min2[0])
        left=min2[0]
        right=min2[1]

        sumlR=left.weight+right.weight
        father=self.Node(None,sumLR)
        father.left=left
        father.right=right

        if data==[]:
            return father

        arr.append(father)

        return makeHuffman(arr)

    def breadth_frist(self,gen,index=0,nextgen=[],result=[]):  #赋默认值
        #广度优先遍历哈弗曼树
        if type(gen)==Node:
            gen=[gen]
        result=[gen[index].data,gen[index].weight]

        if gen[index].left!=None:
            #若左子树不为空
            nextgen.append(gen[index].left)

        if gen[index].right!=None:
            #若右子树不为空
            nextgen.append(gen[index].right)

        if index==len(gen)-1:
            if nextgen==[]:
                #递归结束条件
                return
            else:
                gen=nextgen
                nextgen=[]
                index=0
        else:
            index+=1
        breadth_frist(gen,index,nextgen,result)  #递归
        return result


sourceData = [('a', 8), ('b', 5), ('c', 3), ('d', 3), ('e', 8), ('f', 6), ('g', 2), ('h', 5), ('i', 9),('j', 5), ('k', 7), ('l', 5), ('m', 10), ('n', 9)]

huffman=huffman()
h1 =huffman.makeHuffman(sourceData)
print(huffman.breadth_first(h1))
























