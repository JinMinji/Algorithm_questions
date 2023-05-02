#Contest335, Q2

from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.level_sums = [0 for i in range(1000000)]

    def findChild(self, cur_level, cur_node):
        self.level_sums[cur_level] += cur_node.val
        if cur_node.left:
            self.findChild(cur_level+1, cur_node.left)
        if cur_node.right:
            self.findChild(cur_level+1, cur_node.right)

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # level = int(math.log2(len(root))) + 1
        level = 1
        self.findChild(level, root)
        self.level_sums.sort(reverse=True)
        return self.level_sums[k-1] if self.level_sums[k-1] else -1


if __name__ == '__main__':
    root = TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4, None, None), TreeNode(6, None, None)), TreeNode(1, None, None)), TreeNode(9, TreeNode(3, None, None), TreeNode(7, None, None)))

    root = [101930, 374175, 422101, 762947, 176518, 691682, 123558, None, 966489, None, 757886, 304165, 785988, 183881, 97567,
     None, None, 706308, None, 427069, 676837, 612483, 79201, None, None, None, None, 368085, 495376, 969412, 270644,
     955986, 743171, None, None, None, 966674, 807767, 109351, None, None, 218183, None, None, 705578, 969133, 202997,
     512061, 37634, 865146, None, 603118, None, None, None, 237753, None, 903904, 174402, None, 421931, 118774, 932506,
     964490, 393335, 857568, 467662, None, None, 165622, None, None, None, None, None, None, None, None, 450458, 444621,
     750547, 823529, None, None, 366044, 269454, 477133, None, 172669, None, None, None, None, 399358, None, 344621,
     734654, None, None, None, 163230, None, 834790, None, 575055, None, 779180, None, None, None, 945521, 955975,
     187504, None, 713073, 266922, None, 636977, None, 307423, 354775, None, 904046, None, None, 594127, None, 443557,
     None, 321731, 213475, 656929, None, None, None, None, None, 596001, None, None, 538284, None, 992174, None, None,
     697320, 802658, 121837, None, None, None, None, None, None, None, None, 725228, None, 378862]
    k = 44
    # root = [5,8,9,2,1,3,7,4,6]
    # root = [5, 8, 9, 2, 1, 3, 7, 4, 6]
    # k = 2
    test = Solution()
    answer = test.kthLargestLevelSum(root, k)
    print(answer)