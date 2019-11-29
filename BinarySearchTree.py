#使用链表作为存储方式实现二叉树
class LinkedBinaryTree(BinaryTree):
    #使用链表存储方式实现二叉树
    class Node:
        #定义二叉树的结点
        __slots__ = 'element','parent','left','right'

        def __init__(self):
            self.element=element
            self.parent=parent
            self.left=left
            self.right=right

    class Position(BinaryTree.postion):

        def __init__(self,container,node):
            self.container=container
            self.node=node

        def element(self):

            return self.node.element

        def __eq__(self, other):

            rerurn type(other) is type(self) and other.node is self.node


        def validate(self,p):

            if not isinstance(p,self.Position):
                raise TypeError('p必须是之前位置类型')
            if p.container is not self:
                raise ValueError('P不属于这个容器')
            if p.node.parent is p.node:
                raise ValueError('p is no longer vaild')
            return p.node

        def make_position(self,node):

            return self.Position(self,node) if node is note None else None

