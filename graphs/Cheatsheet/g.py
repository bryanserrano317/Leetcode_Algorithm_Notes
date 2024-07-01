from collections import deque, defaultdict

def topo(graph):
	incomingEdges = defaultdict(int)
	directionMap = defaultdict(list)
	nodeCount = 0
	topo = []

	for u,v in graph:
		incomingEdges[v] += 1
		directionMap[u].append(v)

	stack = []

	for v in range(len(graph)):
		if (incomingEdges[v] == 0):
			topo.append(v)
			stack.append(v)

	while(stack):
		currNode = stack.pop()
		nodeCount += 1

		for v in directionMap[currNode]:
			incomingEdges[v] -= 1
			if(incomingEdges[v] == 0):
				stack.append(v)
				topo.append(v)
	print("Topological sort: " , topo)
	return nodeCount == (len(graph) + 1)

graph = [[0,3] , [2,1], [1,3], [3,4], [4,5], [4,6], [5,7], [2,0]] 
print("""

    2
   / \\
  0   1
   \ /
    3
    |
    4
   / \\
  5   6
   \\
    7


""")

topo(graph)

print("------")

print("""
      
    0 - 1
    |   |
    2 - 3 - 4

""")

def dfs(graph):
    def explore(u):
        stack = []
        stack.append(u)
        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                print("dfs: ", u)
                for v in graph[u]:
                    stack.append(v)
    
    visited = set()
    for i in range(len(graph)):
        if i not in visited:
            explore(i)

def recursive_dfs(graph):
    def explore(u):
        visited.add(u)
        print("recursive dfs: ", u)
        for v in graph[u]:
            if v not in visited:
                explore(v)

    visited = set()
    for i in range(len(graph)):
        if i not in visited:
            explore(i)

from collections import deque
def bfs(u): 
    q = deque()
    q.append(u)
    visited.add(u)
    while q:
        u = q.popleft()
        print("bfs: ", u)
        for v in graph[u]:
            if v not in visited:
                q.append(v)
                visited.add(v)




graph = [[1,2], [0,3], [0,3], [1,2,4], [3]]


dfs(graph)
print("------")
visited = set()
for u in range(len(graph)):
    if u not in visited:
        bfs(u)
print("------")
recursive_dfs(graph)
print("------")

def kosaraju(graph):
    def explore(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                explore(v)
        stack.append(v)
    
    def reverse(graph):
        reversed_graph = [[] for _ in range(len(graph))]
        for u in range(len(graph)):
            for v in graph[u]:
                reversed_graph[v].append(u)
        return reversed_graph
    
    stack = []
    visited = set()

    scc = []
    for u in range(len(graph)):
        if graph[u] == []:
            scc.append([u])
            continue
        if u not in visited:
            explore(u)

    graph = reverse(graph)

    visited.clear()
    
    
    while stack:
        u = stack.pop()
        if u not in visited:
            cc = []
            explore(u)
            for vertex in visited:
                cc.append(vertex)
            scc.append(cc)
    return scc
print("""
0 -------> 1
^          |
|          |
|          |
|          v
3 <--------2 ----> 4

""")
graph = [[1], [2], [3], [0], []]
print("SCC: ", kosaraju(graph))
print("------")

from queue import PriorityQueue

print(
'''
  1 --(2)-- 2
  |         |
 (1)       (4)
  |         |
  0 --(3)-- 3
'''
)

graphW = {
    0: [(1, 1), (3, 3)],
    1: [(0, 1), (2, 2)],
    2: [(1, 2), (3, 4)],
    3: [(0, 3), (2, 4)]
}




def dijkstra(graph, start):
    dist = [float("inf")] * len(graph)
    prev = [None] * len(graph)
    dist[start] = 0

    q = PriorityQueue()
    q.put((start, dist[start]))

    while not q.empty():
        u, u_dist = q.get()
        for v, v_dist in graph[u]:
            minDist = u_dist + v_dist
            if minDist < dist[v]:
                dist[v] = minDist
                prev[v] = u
                q.put((v, dist[v]))
    return dist, prev


dist, shortestPath = dijkstra(graphW , 0)
print("(Dijkstra's): Edges in the Shortest Path from 0:")
for u,v in enumerate(shortestPath):
    print(f"({0}, {u}) with weight {dist[u]}")
print("-----")
# # union-find

class unionFind:
    # makeSet
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [0 for i in range(n)]

    def find(self, u):
        root = u
        while ( root != self.parent[root]):
            root = self.parent[root]

        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]


    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        if self.size[root_u] > self.size[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_u] = root_v
            if self.size[root_u] == self.size[root_v]:
                self.size[root_v] = self.size[root_u] + 1

def kruskal(graph, num_vertices):
    # Sort all edges in the graph by their weight
    edges = sorted(graph, key=lambda edge: edge[2])  # kruskal
    uf = unionFind(num_vertices) # uf
    mst = [] # kruskal

    for u, v, weight in edges: # uf 
        if uf.find(u) != uf.find(v): # uf 
            uf.union(u, v) # uf
            mst.append((u, v, weight)) # kruskal

    return mst


"""
0 - (1) -> 1
|          |
(3)       (2)
|          |
v          v
3 <- (4) - 2

"""
# Example usage:
graph = [
    (0, 1, 1),
    (0, 3, 3),
    (1, 2, 2),
    (2, 3, 4),
]
num_vertices = 4

mst = kruskal(graph, num_vertices)
print("(Kruskal's): Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"({u}, {v}) with weight {weight}")
print("-----")
print("\n", 
"""
MST

0 - (1) -> 1
|          |
(3)       (2)
|          |
v          v
3          2

"""
)


# graphW -->

'''
  1 --(2)-- 2
  |         |
 (1)       (4)
  |         |
  0 --(3)-- 3
'''

graphW = {
    0: [(1, 1), (3, 3)],
    1: [(0, 1), (2, 2)],
    2: [(1, 2), (3, 4)],
    3: [(0, 3), (2, 4)]
}

def prims(graphW, start):
    dist = [float('inf')] * num_vertices
    prev = [None] * num_vertices
    start = 0 # insert start here
    dist[start] = 0
    visited = set()

    q = PriorityQueue()
    q.put((dist[start], start))

    while not q.empty():
        u_dist, u= q.get()
        if u in visited:
            continue

        visited.add(u)

        for v, v_dist in graphW[u]:
            if v not in visited and v_dist < dist[v]:
                dist[v] = v_dist
                prev[v] = u
                q.put((dist[v], v))
    return dist, prev

# alt 

# def prims(graphW, start):
#     q = PriorityQueue()
#     q.put((0, start))  # (weight, vertex)
    
#     total_cost = 0
    
#     while not q.empty():
#         weight, u = q.get()
#         if u in visited:
#             continue
        
#         # Add to MST
#         visited.add(u)
#         total_cost += weight
        
#         # Add all edges from the current vertex to the priority queue
#         for w, v in graph[u]:
#             if v not in visited:
#                 q.put((w, v))
    



dist, shortestPath = prims(graphW , 0)
print("(Prim's): Edges in the Minimum Spanning Tree (MST):")
for u,v in enumerate(shortestPath):
    print(f"({v}, {u}) with weight {dist[u]}")
print("-----")
          

  
##### grid traversals

# ex. number of islands
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print("""
Grid = 
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
""")

def dfs_grid_recursive(x, y, grid):
    def out_of_bounds(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or (x,y) in visited or  grid[x][y] != "1":
            return True
        
    if out_of_bounds(x,y):
        return 
    
    visited.add((x,y))

    directions = [[-1, 0], [1, 0] , [0, -1], [0, 1]]

    for dx, dy in directions:
        dfs_grid_recursive(dx + x, dy + y, grid)
    
visited = set()
res = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == '1' and (x,y) not in visited:
            dfs_grid_recursive(x, y, grid)
            res += 1

print("(dfs grid traversal recursive) num islands: ", res)

def dfs_grid_iterative(x, y, grid):
    def out_of_bounds(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or (x,y) in visited or grid[x][y] != "1":
            return True

    stack = []
    stack.append((x,y))
    directions = [(-1, 0), (1, 0) , (0, -1), (0, 1)]

    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            if not out_of_bounds(dx + x, dy + y):
                stack.append((dx + x, dy + y))
                visited.add((dx + x, dy + y))
    
visited = set()
res = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if (x,y) not in visited and grid[x][y] == "1":
            dfs_grid_iterative(x, y, grid)
            res += 1


print("(dfs grid traversal iterative) num islands: ", res)

def bfs_grid_iterative(x, y, grid):
    def out_of_bounds(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or (x,y) in visited or grid[x][y] != "1":
            return True

    q = deque()
    q.append((x,y))
    directions = [(-1, 0), (1, 0) , (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            if not out_of_bounds(dx + x, dy + y):
                q.append((dx + x, dy + y))
                visited.add((dx + x, dy + y))
    
visited = set()
res = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if (x,y) not in visited and grid[x][y] == "1":
            bfs_grid_iterative(x, y, grid)
            res += 1


print("(bfs grid traversal iterative) num islands: ", res)