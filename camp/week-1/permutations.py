class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def is_valid_state(state):
            return len(state) == len(nums)
        
        def get_candidates(state):
            
            global_state = [num for num in nums if num not in state]
            
            return global_state
        
        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                
            for candidate in get_candidates(state):
                state.append(candidate)
                search(state, solutions)
                state.remove(candidate)
    
        solutions = []
        state = []
        search(state, solutions)
        return solutions