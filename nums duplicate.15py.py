class Solution:
 def containsDuplicate(self, nums: List[int]) -> bool:
  ls=len(set(nums))
  l=len(nums)
  return l>ls