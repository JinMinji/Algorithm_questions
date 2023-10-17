# Contest362, Q2

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_gap = abs(fx - sx)
        y_gap = abs(fy - sy)
        
        if x_gap == 0 and y_gap == 0 and t == 1:
            return False
        if t >= max(x_gap, y_gap):
            return True

        return False
        

if __name__ == "__main__":
    test = Solution()
    print(test.isReachableAtTime(sx = 1, sy = 1, fx = 2, fy = 1, t = 1))
    print(test.isReachableAtTime(sx = 1, sy = 2, fx = 1, fy = 2, t = 1))
    print(test.isReachableAtTime(sx = 1, sy = 1, fx = 2, fy = 2, t = 1))
    print(test.isReachableAtTime(sx = 1, sy = 1, fx = 2, fy = 1, t = 2))
    print(test.isReachableAtTime(sx = 1, sy = 1, fx = 1, fy = 1, t = 3))
    print(test.isReachableAtTime(sx = 2, sy = 4, fx = 7, fy = 7, t = 6))
    print(test.isReachableAtTime(sx = 3, sy = 1, fx = 7, fy = 3, t = 3))
    print(test.isReachableAtTime(sx = 1, sy = 3, fx = 1, fy = 3, t = 0))

