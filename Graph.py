
#广度遍历
def BFS(graph,source):
    fronts=[source]
    travel=[source]

    while fronts:
        nexts=[]
        for front in fronts:
            for current in graph[front]:
                if current not in travel:
                    travel.append(current)
                    nexts.append(current)

                fronts=nexts

        return travel

#深度遍历
def DFS(graph,source):

    travel=[]
    stack=[source]

    while stack:
        current=stack.pop()
        if current not in travel:
            travel.append(current)

        for next_adj in graph[current]:
            if next_adj not in travel:
                stack.append(next_adj)
    return travel

if __name__ == "__main__":
    graph = {}
    graph['a'] = ['b']
    graph['b'] = ['c', 'd']
    graph['c'] = ['e']
    graph['d'] = []
    graph['e'] = ['a']

    # 测试
    print(BFS(graph, 'b'))
    print(DFS(graph, 'b'))

