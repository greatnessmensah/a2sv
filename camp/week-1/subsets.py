class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def is_valid_state(state):
            return len(state) < len(nums)+1
        
        def get_candidates(state):
            if len(state) == 0:
                global_state = set([i for i in nums])
            else:
                global_state = set([i for i in nums if i > max(state)])
                
            return global_state.difference(state)
        
        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                
            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)

        solutions = []
        state = set()
        search(state, solutions)
        
        
        return solutions
