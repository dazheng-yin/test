#平衡二叉树
class Node:
    #平衡二叉树的结点
    __slots__ = 'value','lc','rc','lh','rh'

    def __init__(self):
        self.value=None
        self.lc=None
        self.rc=None
        self.lh=0
        self.rh=0

class AVL:
    #平衡二叉树
    def __init__(self):
        self.root=False
        self.front_list=[]
        self.middle_list=[]
        self.after_list=[]

    def creat_AVL(self,n=0,arr):
        #创建二叉平衡树
        if arr=[]:
            print("创建失败")
            return

        if n>len(arr)-1:
            #创建完成
            return

        node=Node()
        node.value=arr[n]

        if not self.root:
            self.root=node

        else:
            #插入结点
            add_node(self.root,node)

        creat_AVL(n+1,arr)

    def add_node(self,parent,newNode):
        #向二叉平衡树种插入结点
        if newNode.value<parent.value:
            if parent.lc==None:
                parent.lc=newNode
                parent.lh=1

            else:
                add_node(parent.rc,newNode)
                parent.rh=max(parent.rc.lh,parent.rc.rh)+1

                if parent.rh-parent.lh>=2:
                    self.right_avertance(parent)

        if newNode.value>parent.value:
            if parent.rc==None:
                parent.rc=newNode
                parent.rh=1

            else:
                add_nede(parent.lc,newNode)
                parent.lh=max(parent.lc.lh,parent.lc.rh)+1

                if parent.lh-parent.rh>=2:
                    self.left_avertance(parent)


    def up_high(self,node):
        #平衡二叉树结点下高度更新
        #初始化结点高度
        node.lh=0
        node.rc=0

        if node.rc==None and node.lc==None:
            #叶子结点
            return

        if node.rc:
            self. up_high(node.rc)

            node.rh=max(node.rc.lh,node.rc.lh)+1

        if node.lc:
            self.up_high(node.lc)
            node.lh=max(node.lc.lh,node.lc.rh)+1

        if node.lh-node.rh>=2:
            self.left_avertance(node)

        if node.rh-node.lh>=2:
            self.right_avertance(node)


    def best_LeftRight(self,node,type=0):
        #返回最左或最右的结点
        #type==0时查找最右

        if type==0:
            if node.lc==None:
                return
            elif node.lc.rc==None:
                return

            else:
                return self.best_LeftRight(node.lc,type)

        else:
            if node.rc==None:
                return
            elif node.rc.lc==None:
                return

            else:
                return self.best_LeftRight(node.rc,type)

    def left_avertance(self,node):
        #进行左偏的调试
        newNode.value=node.value
        newNode.rc=node.rc
        best_right=self.best_LeftRight()








                    _































