'''
DMS QUESTION 6
'''
def comp_graph(graph):# DEFAULT FUNCTION
    num_vertices = len(graph)

    # Check if each vertex is connected to all other vertices
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and graph[i][j] != 1:#CHECKS FOR THE CONNECTION OF EACH VERTEX TO EVERY OTHER VERTEX
                return False

    return True


# let adjancey matrix G be :
G = [[0, 1, 1, 1],
     [1, 0, 1, 1],
     [1, 1, 0, 1],
     [1, 1, 1, 0]]
print("LENGTH",len(G))
result = comp_graph(G)
if result:
    print("The graph is a complete graph")
else:
    print("The graph is not a complete graph")

