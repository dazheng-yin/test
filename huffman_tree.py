#哈弗曼树
class huffman_tree:

    class Node:
        #定义结点
        def __init__(self,data,weight):

            self.data=data
            self.weight=weight
            self.left=None
            self.right=None

    def make_huffman(self,source):
        #使用递归的方法来生成哈弗曼树
        min_2,data=min_two(source)
        print(min_2[0].data,min_2[1].data)
        left=min_2[0]
        right=min_2[1]

        sumLR=left.weight+right.weight
        father=self.Node(None,sumLR)
        father.left=left
        father.right=right

        if data==[]:
            #递归结束的条件
            return father
        data.append(father)

        return make_huffman(data)   #递归生成哈夫曼树


    def min_two(self,arr):
        #选择出权值最小的结点的方法

        min_2=[Node(None,float('inf')),Node(None,float('inf'))]   #用于记录权值最小的两个结点
        arr2=[]

        for i in range(len(arr)):
            #找出最小的两个值
            if arr[i].weight<min_2[0].weight:
                #若给定的数据中权值小于min_2-0的权值
                if min_2[0].weight!=float('inf'):
                    arr2.append(min_2[0])

                min_2[0],min_2[1]=arr[i],min[0]

            elif arr[i].weight<min_2[1].weight:

                if min_2[1]!=float('inf'):
                    arr2.append(min_2[1])

                min_2[1]=arr[i]

            else:
                arr2.append(arr[i])

        return min_2,arr2
        #min_2中是权值最小的两个值，arr2中是其他权值较大的节点

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

sourceData = [('a', 8), ('b', 5), ('c', 3), ('d', 3), ('e', 8), ('f', 6), ('g', 2), ('h', 5), ('i', 9), ('j', 5), ('k', 7), ('l', 5), ('m', 10), ('n', 9)]
sourceData = [BinaryTree(x[0], x[1]) for x in sourceData]

huffman=huffman_tree()
h1 =huffman.make_huffman(sourceData)
print(huffman.breadth_first(h1))
































