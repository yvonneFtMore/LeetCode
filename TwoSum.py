# -*- coding: utf-8 -*-


class Solution:

    def __init__(self, arr, target):
        self.nums = arr.split(',')
        self.target = int(target)
        print self.nums, self.target

    def TwoSum(self):
        for i in range(len(self.nums)):
            for j in range(1, len(self.nums)):
                if int(self.nums[i]) + int(self.nums[j]) == self.target:
                    return i, j

if __name__ == '__main__':
    array = raw_input("Please input a list of numbers:")
    target = raw_input("Please input the target:")
    slt = Solution(array, target)
    n, k = slt.TwoSum()
    print n, k