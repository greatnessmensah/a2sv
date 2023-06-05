class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        
        for i in nums:
            hashmap[i] += 1
            
        for key, value in hashmap.items():
            if value > (len(nums) / 2):
                return key
