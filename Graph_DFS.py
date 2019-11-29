#图的广度优先
# 图的宽度遍历和深度遍历

#广度优先
def BFS(graph, source):

    fronts = [source]     # 表示前驱节点
    travel = [source]       # 表示遍历过的节点
    # 当前驱节点为空时停止遍历
    while fronts:
        nexts = []          # 当前层的节点（相比frontier是下一层）
        for front in fronts:
            for current in graph[front]: # 遍历当前层的节点
                if current not in travel:   # 判断是否访问过
                    travel.append(current)  # 没有访问过则入队
                    nexts.append(current)   # 当前结点作为前驱节点
        fronts = nexts   # 更改前驱节点列表
    return travel


#深度优先
def DFS(graph, source):

    travel = []     # 存放访问过的节点的列表
    stack = [source]      # 构造一个堆栈
    while stack:            # 堆栈空时结束
        current = stack.pop()       # 堆顶出队
        if current not in travel:   # 判断当前结点是否被访问过
            travel.append(current)  # 如果没有访问过，则将其加入访问列表
        for next_adj in graph[current]: # 遍历当前结点的下一级
            if next_adj not in travel:  # 没有访问过的全部入栈
                stack.append(next_adj)
    return travel


if __name__ == "__main__":
    graph = {}
    graph['a'] = ['b']
    graph['b'] = ['c','d']
    graph['c'] = ['e']
    graph['d'] = []
    graph['e'] = ['a']


    #测试
    print(BFS(graph, 'b'))

    print(DFS(graph, 'b'))