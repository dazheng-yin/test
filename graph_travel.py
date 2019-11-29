#图的遍历
class graph_travel(object):

    def BFS(self,graph,source):
        #广度遍历
        fronts=[source]
        travels=[source] #已遍历的结点

        while fronts:
            next=[]

            for front in fronts:
                for current in graph[front]:
                    if current not in travels:
                        next.append(current)
                        travels.append(current)

            fronts=next

        return travels

    def DFS(self,graph,source):
        #深度遍历
        stack=[source]
        travel=[]

        while stack:
            current=stack.pop()

            if current not in travel:
                travel.append(current)

            for next in graph[current]:
                if next not in travel:
                    stack.append(next)

        return travel


if __name__=="__main__":
    #测试
    graph={}
    graph['a'] = ['b']
    graph['b'] = ['c', 'd']
    graph['c'] = ['e']
    graph['d'] = []
    graph['e'] = ['a']


    G=graph_travel()

    #广度
    print(G.BFS(graph, 'e'))
    #深度
    print(G.DFS(graph, 'b'))
























