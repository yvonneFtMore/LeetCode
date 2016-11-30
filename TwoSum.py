# -*- coding: utf-8 -*-


class Solution(object):

    def __init__(self, arr, target):
        self.nums = arr.split(',')
        self.target = int(target)
        print self.nums, self.target

    def two_sum(self):
        dict = {}
        for i in xrange(len(self.nums)):
            x = int(self.nums[i])
            if target - x in dict:
                return dict[target - x], i
            dict[x] = i

if __name__ == '__main__':
    array = raw_input("Please input a list of numbers:")
    target = raw_input("Please input the target:")
    slt = Solution(array, target)
    n, k = slt.two_sum()
    print n, k