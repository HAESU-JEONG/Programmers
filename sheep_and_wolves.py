def DFS(graph, start, visited):
    # visited.append(start)
    # for node in graph[start]:
    #     if node not in visited:
    #         DFS(graph, node, visited)
    # return visited

    # 위의 내용은 기본 DFS 코드

    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            DFS(graph, node, visited)
    return visited



def solution(info, edges):
    for i in range(len(info)):
        if info[i] == 0: # 양은 1로 값 변경
            info[i] = 1
        else: # 늑대는 -1로 값 변경
            info[i] = -1

    
    graph = [[] for _ in range(len(info))]
    
    for i in range(len(edges)):
        graph[edges[i][0]].append(edges[i][1])

    # for i in range(len(info)):
    #     print('graph[{}] = {}'.format(i, info[i]))
    #     for j in range(len(graph[i])):
    #         print('graph[{}]의 인접 리스트 : {} '.format(i, graph[i][j]))

    # 위의 주석처리된 코드는 그래프 확인용. 

    # 여기까지 양과 늑대 그래프 생성된 상태임.


    visited = []
    print(DFS(graph, 0, visited))
