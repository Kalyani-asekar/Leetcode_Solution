class Solution:
    def reverse(self, x: int) -> int:
        y=x
        sign= -1 if y<0 else 1
        rev=0
        y=abs(y)
        while y >0:
            digit=y%10
            rev=rev*10+digit
            y//=10
        rev*=sign
        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev

        