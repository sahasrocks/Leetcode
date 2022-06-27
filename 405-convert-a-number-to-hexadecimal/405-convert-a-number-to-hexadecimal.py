class Solution:
    def toHex(self, num: int) -> str:
        if num==0: return '0'       # base condition
        if num<0: num+=2**32        # 2s complement
        hexcode='0123456789abcdef'  # index from hexcode returns required character
        ans = ''
        while num:
            num,r=divmod(num,16)
            ans = hexcode[r]+ans    # LSB at the end of the string
        return ans