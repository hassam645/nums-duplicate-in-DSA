class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:

        duplicate = set()

        for num in nums:

            if num in duplicate:

                return True

            duplicate.add(num)

        return False