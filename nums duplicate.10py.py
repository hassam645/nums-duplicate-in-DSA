class Solution:

 def containsDuplicate(self, nums: List[int]) -> bool:

setArray=set()

for i in nums:

if i in setArray:

return true

else:
setArray.add(i)
return false