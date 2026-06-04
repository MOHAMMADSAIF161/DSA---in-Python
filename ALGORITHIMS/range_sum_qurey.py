from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        

    def sumRange(self, left: int, right: int) -> int:
        subarray=self.nums[left:right+1]
        total=0
        for num in subarray:
            total+=num
        return total
n=NumArray([1,2,3,4])
p=n.sumRange(0,2)