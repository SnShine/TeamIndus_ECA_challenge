graph = {"A": ["B", "E"],
         "B": ["A", "C"],
         "C": ["B", "D", "E"],
         "D": ["C", "E"],
         "E": ["A", "C", "D"]}


def find_all_paths(node, destination, visited, graph, path):
    visited[node] = True
    path.append(node)

    if node == destination:
        print [destination] + path

        # if you don't want many
        # return
    else:
        for i in graph[node]:
            if visited[i] == False:
                find_all_paths(i, destination, visited, graph, path)

    visited[node] = False
    path.pop()

visited = {}
for i in graph:
    visited[i] = False

path = []

find_all_paths("E", "A", visited, graph, path)
