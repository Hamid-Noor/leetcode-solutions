class Solution:
    import math
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        x = math.log2(n)
        f_x = math.floor(x)
        c_x = math.ceil(x)
        if f_x==c_x:
            return True
        else:
            return False
        
