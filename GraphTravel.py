#图的遍历

#深度优先遍历
def DFS(graph,source):
    #使用栈实现深度优先遍历
    stack=[source]
    travel=[]

    while stack:
        #深度遍历的关键步骤
        current=stack.pop()

        if current not in travel:
            travel.append(current)

        for next in graph[current]:
            if next not in travel:
                stack.append(next)

    return travel

#广度优先遍历
def BFS(graph,source):
    #广度优先可以使用队列，也可以一层一层的遍历
    fronts=[source]
    travel=[source]

    while fronts:
        next=[]

        for front in fronts:
            for current in graph[front]:
                if current not in travel:
                    travel.append(current)
                    next.append(current)

        fronts=next

    return travel

if __name__ == "__main__":
    graph = {}
    graph['a'] = ['b']
    graph['b'] = ['c', 'd']
    graph['c'] = ['e']
    graph['d'] = []
    graph['e'] = ['a']

   

    print(BFS(graph, 'e'))

    print(DFS(graph, 'b'))

