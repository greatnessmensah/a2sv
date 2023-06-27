class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # return len(set([int(str(num)[::-1]) for num in nums] + nums))

        hashset = set()
        
        for i in range(len(nums)):
            reverse = int(str(nums[i])[::-1])
            hashset.add(nums[i])
            
            if reverse not in hashset:
                hashset.add(reverse)
                
        return len(hashset)
