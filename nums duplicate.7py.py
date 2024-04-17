from types import TracebackType
class solution:
 def containsduplicate(self, nums: list[int]) -> bool:
l=set()
for i in nums:
if(i not in l):
  l.add(i)
else:
return True
return false