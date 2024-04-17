class solution:
 def containsduplicate(self, nums: list[int]) -> bool:
  hashset=set()
  for num in nums:
if num in hashset:
return True
else:
hashset.add(num)
return false