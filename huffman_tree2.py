#哈弗曼树复现

class huffman_tree:
    #哈弗曼树类
    class Node:
        #定义哈弗曼树结点
        def __init__(self,data,weight):
            self.data=data
            self.weight=weight
            self.left=left
            self.right=right

    def min(self,data):
        #此函数找到权值最小的两个结点
        min2=[Node(None,float('inf')),Node(None,float('inf'))]
        arr=[]

        for i in range(len(data)):
            if min2[0].weight>data[i]:
                if min2[0].weight!=float('inf'):
                    arr.append(min2[0])

                min2[0],min2[1]=data[i],min2[0]

            elif data[i].weight<min2[1].weight:
                if min2[i].weight!=float('inf'):
                    arr.append(min2[1])

                min2[1]=data[i]

            else:
                arr.append(data[i])

        return min2,arr

    def make_huffman(self,source):
        #生成哈弗曼树
        min2,arr=min(source)
        print(min2[0],min2[1])
        left =min2[0]
        right=min2[1]

        sumlr=left.weight+right.weight
        father=Node(None,sumlr)
        father.left=left
        father.right=right

        if data=[]:
            return father

        arr.append(father)

        return make_huffman(arr)

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

        if index=len(gen)-1:
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

sourceData = [('a', 8), ('b', 5), ('c', 3), ('d', 3), ('e', 8), ('f', 6), ('g', 2), ('h', 5), ('i', 9), ('j', 5), ('k', 7), ('l', 5), ('m', 10), ('n', 9)]
sourceData = [BinaryTree(x[0], x[1]) for x in sourceData]

huffman=huffman_tree()
h1 =huffman.make_huffman(sourceData)
print(huffman.breadth_first(h1))























