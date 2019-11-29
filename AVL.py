#平衡二叉树

class Node:
    #平衡二叉树的结点
    def __init__(self):

        self.lc=None    #左孩子
        self.rc=None    #右孩子
        self.lh=0   #左子树高度
        self.rh=0   #右子树高度
        self.value=None

class AVL:
    #平衡二叉树的建立与操作
    def __init__(self):
        self.root=False
        self.front_list=[]
        self.middle_list=[]
        self.after_list=[]

    def creat_tree(self,n,arr):
        #创建二叉树
        if arr==[]:
            print("创建失败，输入列表为空！")
            return

        if n>len(arr)-1:
            print("创建完成")
            return

        node=Node()
        node.value=arr[n]

        if not self.root:
            self.root=node
            self.list=arr      #??????什么意思

        else:
            self.add(self.root,node)

        self.creat_tree(n+1,arr)

    def add_node(self,parent,new_node):
        #向二叉树增加结点
        if new_node.value>parent.value:
            #若新插入的结点的值大于父节点的值，应该为该父节点的右孩子
            if parent.rc==None:
                #如果该父节点的
                parent.rc=new_node
                #该父节点右子树高度为1
                parent.rh=1

            else:
                #该父节点的有右孩子
                add_node(parent.rc,new_node)
                #插入成功后，计算父节点的右子树高度
                parent.rh=max(parent.rc.rh,parent.rc.lh)+1

                if parent.rh-parent.lh>=2:
                    self.right_avertence(parent)


        else:
            #新插入的结点值小于父节点，插入父节点的左边
            if parent.lc==None:
                #左子树为空
                parent.lc=new_node
                #左子树高度
                parent.lh=1

            else:
                #该父节点的左孩子不为空
                add_node(parent.lc,new_node)
                #插入成功后更新左子树的高度
                parent.lh=max(parent.lc.lh,parent.lc.rh)+1

                if parent.lh-parent.rh>=2:
                    #判断子树的偏置
                    self.left_avertence(parent)


    def update_higher(self,node):
        #更新当前结点的高度

        #初始化当前结点的左右子树高度
        node.lh=0
        node.rc=0

        if node.rc==None and node.lc==None:
            #左右子树为空
            return

        else:
            #若不为空，分开讨论
            if node.lc:
                self.update_higher(node.left_children)
                # 当前节点的高度等于左右子节点高度的较大值 + 1
                node.left_height = max(node.left_children.left_height, node.left_children.right_height) + 1
            if node.right_children:
                self.update_higher(node.right_children)
                # 当前节点的高度等于左右子节点高度的较大值 + 1
                node.right_height = max(node.right_children.left_height, node.right_children.right_height) + 1
                # 检查是否仍有不平衡
            if node.left_height - node.right_height >= 2:
                self.left_avertence(node)
            elif node.left_height - node.right_height <= -2:
                self.right_avertence(node)

    def best_left_right(self, node, type=0):
        # 返回node节点最左（右）子孙的父级
        if type == 0:
            if node.left_children == None:
                return node
            elif node.left_children.left_children == None:
                return node
            else:
                return self.best_left_right(node.left_children, type)
        else:
            if node.right_children == None:
                return node
            elif node.right_children.right_children == None:
                return node
            else:
                return self.best_left_right(node.right_children, type)

    def right_avertence(self, node):
        # 右偏 就将当前节点的最左节点做父亲
        new_node = Node()
        new_node.value = node.value
        new_node.left_children = node.left_children
        best_left = self.best_left_right(node.right_children)
        v = node.value
        # 返回的对象本身,
        if best_left == node.right_children and best_left.left_children == None:
            # 说明当前节点没有有节点
            node.value = best_left.value
            node.right_children = best_left.right_children
        else:
            node.value = best_left.left_children.value
            best_left.left_children = best_left.left_children.right_children
        node.left_children = new_node
        self.update_higher(node)

    # 处理左偏情况
    def left_avertence(self, node):
        new_code = Node()
        new_code.value = node.value
        new_code.right_children = node.right_children
        best_right = self.best_left_right(node.left_children, 1)
        v = node.value
        # 返回的对象本身,
        if best_right == node.left_children and best_right.right_children == None:
            # 说明当前节点没有有节点
            node.value = best_right.value
            node.left_children = best_right.left_children
        else:
            node.value = best_right.right_children.value
            best_right.right_children = best_right.right_children.left_children
        node.right_children = new_code
        self.update_higher(node)

    def del_node(self, v, node=None):
        if node == None:
            node = self.root
            # 删除根节点
            if node.value == v:
                self.del_root(self.root)
                return
        # 删除当前节点的左节点
        if node.left_children:
            if node.left_children.value == v:
                self.del_left(node)
                return
        # 删除当前节点的右节点
        if node.right_children:
            if node.right_children.value == v:
                self.del_right(node)
                return
        if v > node.value:
            if node.right_children:
                self.del_node(v, node.right_children)
            else:
                print("删除的元素不存在")
        else:
            if node.left_children:
                self.del_node(v, node.left_children)
            else:
                print("删除的元素不存在")
        # 删除当前节点的右节点

    def del_right(self, node):
        # 情况1 删除节点没有右枝
        if node.right_children.right_children == None:
            node.right_children = node.right_children.left_children
        else:
            best_left = self.best_left_right(node.right_children.right_children)
            # 表示右枝最左孙就是右枝本身
            if best_left == node.right_children.right_children and best_left.left_children == None:
                node.right_children.value = best_left.value
                node.right_children.right_children = best_left.right_children
            else:
                node.right_children.value = best_left.left_children.value
                best_left.left_children = best_left.left_children.right_children
        # 删除当前节点的左节点

    def del_left(self, node):
        # 情况1 删除节点没有右枝
        if node.left_children.right_children == None:
            node.left_children = node.left_children.left_children
        else:
            best_left = self.best_left_right(node.left_children.right_children)
            # 表示右枝最左子孙就是右枝本身
            if best_left == node.left_children.right_children and best_left.left_children == None:
                node.left_children.value = best_left.value
                node.left_children.right_children = best_left.right_children
            else:
                node.left_children.value = best_left.left_children.value
                best_left.left_children = best_left.left_children.right_children
        # 删除根节点

    def del_root(self, node):
        if node.right_children == None:
            if node.left_children == None:
                node.value = None
            else:
                self.root = node.left_children
        else:
            best_left = self.best_left_right(node.right_children)
            # 表示右枝最左子孙就是右枝本身
            if best_left == node.right_children and best_left.left_children == None:
                node.value = best_left.value
                node.right_children = best_left.right_children
            else:
                node.value = best_left.left_children.value
                best_left.left_children = best_left.left_children.right_children






