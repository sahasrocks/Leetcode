class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ""
        for i in num:
            s+=str(i)
        str_list = " ".join(str(int(s)+k)).split()
        final_list = list(map(int,str_list))
        return final_list