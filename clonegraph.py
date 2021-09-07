# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# given a reference of a node in a connected undirected graph
# return a "deep copy" of the graph 
# each node in the graph contains a value (int) and a list (List[Node]) of its neighbors

#class Node {
#   public int val;
#    public List<Node> neighbors;
#}

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

# adjacency list

# dfs (simplier solution)

from typing import List

"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None
    else: []
"""

class Solution:
    
    def __init__(self):
        self.visited = {}
        
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        
        if node in self.visited:
            return self.visited[node]
        
        clone_node = Node(node.val, [])
        
        self.visited[node] = clone_node
        
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
            
        return clone_node

# bfs solution (teaches toplogical sort which will be used for later)

from collections import deque 
class Solution(object):

    def cloneGraph(self, node):
        if not node:
            return node
        
        visited = {}

        queue = deque([node])

        visited[node] = Node(node.val, [])

        while queue:

            n = queue.popleft()

            for neighbor in n.neighbors:
                if neighbor not in visited: 
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
            visited[n].neighbors.append(visited[neighbor])

        return visited[node]


def cloneGraph(self, node: 'Node') -> 'Node':
    # [[2,4], [1,3], [2,4], [1,3]]

    # we have initialized ref node
    if not node: return None
    seen = {} # value: node itself
    def dfs(node, seen): 
        new_node = Node(node.val)
        seen[node.val] = new_node
        new_neighbors = []

        for n in node.neighbors:
            if n.val not in seen:
                new_neighbors.append(dfs(n, seen))
            else:
                new_neighbors.append(seen[n.val])
        new_node.neighbors = new_neighbors
        return new_node
    
    return dfs(node, seen)
