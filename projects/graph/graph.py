"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:  # Raise defines what error and gives the error to the user
            raise IndexError("That vertex does not exist!")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        create a queue
        create list of visited nodes
        put starting node in the queue
        While: queue not empty
        pop first node out of queue
        if not visited
            mark as visited
            get adjacent edges and add to list
        get to top of loop 
        """
        queue = Queue()
        # set() is used to convert any of the iterable to the distinct element and sorted sequenece of iterable elements, commmonly called set.
        visited_nodes = []
        queue.enqueue(starting_vertex)
        while queue.size() > 0:  # while queue isnt empty...
            vertex = queue.dequeue()
            if vertex not in visited_nodes:  # if the vertex has not been visited...
                # add the vertex as a visited node
                visited_nodes.append(vertex)
                # mark the vertex as visited and get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    queue.enqueue(next_vert)
        print(", ".join(str(i) for i in visited_nodes))

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited_nodes = []
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited_nodes:
                visited_nodes.append(vertex)
                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)
        print(", ".join(str(i) for i in visited_nodes))

    def dft_recursive(self, starting_vertex, visited_nodes=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited_nodes.append(starting_vertex)
        for next_vert in self.vertices[starting_vertex]:
            if next_vert not in visited_nodes:
                self.dft_recursive(next_vert, visited_nodes)
        printStatement = ", ".join(str(i) for i in visited_nodes)
        return printStatement
        # print(", ".join(str(i) for i in visited_nodes))

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # queue = Queue()
        # visited_nodes = []
        # queue.enqueue(starting_vertex)
        # while destination_vertex not in visited_nodes:
        #     vertex = queue.dequeue()
        #     if vertex not in visited_nodes:
        #         visited_nodes.append(vertex)
        #         for next_vert in self.vertices[vertex]:
        #             queue.enqueue(next_vert)
        # print(visited_nodes)
        # Create an empty Q and ENQ to the starting vertex

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
