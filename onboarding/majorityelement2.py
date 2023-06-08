class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        t = n // 3
        nums.sort()
        result = []
        left, right = 0, 0

        while right < n:
            count = 0
            while right < n and nums[right] == nums[left]:
                count += 1
                right += 1

            if count > t:
                result.append(nums[left])

            left = right

        return result
