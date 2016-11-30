# -*- coding: utf-8 -*-


class Solution(object):

    def __init__(self, x):
        self.num = int(x)

    def reverse(self):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        reverse_num = 0
        if self.num < 0:
            self.num = -self.num
            flag = True
        while self.num:
            n = self.num % 10
            self.num = self.num / 10
            reverse_num = n + reverse_num * 10
        if reverse_num > 2147483647:
            # because of the python2 will automatically turn int into long, so we just add the limit personally
            return 0
        if flag:
            return -reverse_num
        return reverse_num

if __name__ == '__main__':
    num = raw_input("Please input the number you want to reverse:")
    slt = Solution(num)
    re = slt.reverse()
    print re