class solution:
def containduplicate(self,nums: list[int])->bool:
  return len(set(nums))!=len(nums)