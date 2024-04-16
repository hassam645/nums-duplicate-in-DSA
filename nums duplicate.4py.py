class solution(object):
def containduplicate(self,nums):
hset=set()
for idx in nums:
if idx in hset:
    return True
else:
    hset.add(idx)