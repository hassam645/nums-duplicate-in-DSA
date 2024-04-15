class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
nums.sort()
n=len(nums)
for i in range(1,n):
    if num[i]==num[i-1]:
        return true
    return false