def island_counter(matrix):
    # create a visited matrix
    visited = []
    for i in range(len(matrix)):  # if we visit an island it will be change false to true
        visited.append([False] * len(matrix[0]))

    island_count = 0

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # if not visited
            if not visited[x][y]:
                if matrix[x][y] == 1:
                    # Find the neighbors - run some DF and mark each as visited

                    island_count += 1
    return island_count
