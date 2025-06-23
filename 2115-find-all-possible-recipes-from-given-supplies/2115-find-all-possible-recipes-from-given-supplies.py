class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list) #recipe --> dependent recipe
        indegrees = {}
        supplies = set(supplies) #for O(1) search

        #make adj list and indegree map
        for i in range(len(recipes)):
            recipe = recipes[i]
            indegrees[recipe] = 0 #initialized at 0
            for ing in ingredients[i]:
                if ing not in supplies:
                    adj[ing].append(recipe)
                    indegrees[recipe] += 1
        
        #initialize queue w recipes of 0 indegree
        queue = deque([recipe for recipe, degree in indegrees.items() if degree == 0])

        #topological sort (BFS)
        result = []
        while queue:
            curr = queue.popleft() 
            result.append(curr)
            for next_rec in adj.get(curr, []):
                indegrees[next_rec] -= 1 #remove indegree from curr's dependents
                if indegrees[next_rec] == 0:
                    queue.append(next_rec)
        
        return result
