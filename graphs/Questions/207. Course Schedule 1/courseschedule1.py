# Iterative DFS

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses: return True
        preq_dict = defaultdict(list)
        black = set()
        for c,p in prerequisites:
            preq_dict[c].append(p)
        for start in range(numCourses):   
            stack = []
            stack.append(start)
            grey = set()
            grey.add(start)
            while stack:
                curr = stack.pop()
                if curr in preq_dict:
                    for preq in preq_dict[curr]:
                        if preq == start:
                            return False
                        if preq not in grey and preq not in black:
                            grey.add(preq)
                            stack.append(preq)
                black.add(start)
        return True

# Recursive DFS

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True

        adjList = { i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visited = set()

        def dfs(course): # we're going to be at a course # the course is not a prereq for the preqs # in other words, there's a cycle
            if course in visited:
                return False
            if adjList[course] == []:
                return True
            
            visited.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adjList[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

# Topological Sort

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses: return True
        preq_dict = defaultdict(list)
        black = set()
        for c,p in prerequisites:
            preq_dict[c].append(p)
        for start in range(numCourses):   
            stack = []
            stack.append(start)
            grey = set()
            grey.add(start)
            while stack:
                curr = stack.pop()
                if curr in preq_dict:
                    for preq in preq_dict[curr]:
                        if preq == start:
                            return False
                        if preq not in grey and preq not in black:
                            grey.add(preq)
                            stack.append(preq)
                black.add(start)
        return True