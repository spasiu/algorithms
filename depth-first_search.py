SAMPLE_GRAPH = {1:[2,3,4], 
                2:[5,6,7,8], 
                3:[9], 
                4:[10], 
                5:[9], 
                6:[3,4], 
                7:[2,11], 
                8:[9], 
                9:[1,2,3,4], 
                10:[6], 
                11:[]} #sample value

START = 1 #sample value

#globals
graph = SAMPLE_GRAPH
start = START
visited = []

def visit(node):
    visited.append(node)
    return graph[node]

def check_visited(node):
    return node not in visited

def generate_list(node):
    return filter(check_visited, visit(node))

def iterator(node):
    connections = generate_list(node)
    for connection in connections:
        iterator(connection)

iterator(start)        
print visited

