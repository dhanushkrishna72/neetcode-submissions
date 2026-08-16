class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        newList = []
        l,r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                newList.append(l+1)
                newList.append(r+1)
                return newList
            elif(total < target):
                l = l +1
            else:
                r = r -1
        return newList