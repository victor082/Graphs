from util import Stack, Queue


def dfs(starting_vertex, destination_vertex):
    stack = Stack()
    visited = set()
    stack.push([starting_vertex])

    while stack.size() > 0:
        path = stack.pop()
        vertex = path[-1]
        if vertex not in visited:
            visited.append(vertex)
        for next_vert in self.vertices[vertex]:
            new_path = list(path)
            new_path.append(next_vert)
            stack.push(new_path)
    return visited[-1]


def earliest_ancestor(ancestors, starting_node):
    ancestry = []
