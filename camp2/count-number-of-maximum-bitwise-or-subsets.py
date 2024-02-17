class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        
        for i in range(1, len(nums) + 1):
            subsets = combinations(nums, i)
            for elem in subsets:
                res = 0
                for num in elem:
                    res |= num
                hashmap[res] += 1
                
        return hashmap[max(hashmap.keys())]
