# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

import heapq

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        heap_nums = []
        for element in nums:
            if element not in seen:
                print(f"Element: {element}")
                seen.add(element)
                heapq.heappush(heap_nums, element * -1)

        print(f"Seen: {seen}")
        print(f"Heap: {heap_nums}")

        if len(heap_nums) < 3:
            return heap_nums[0] * -1
        else:
            for _ in range(2):
                heapq.heappop(heap_nums)
            return heapq.heappop(heap_nums) * -1


solution = Solution()
input = [3,2,1]
result = solution.thirdMax(input)
print(f"Input: {input}; Result: {result}")
