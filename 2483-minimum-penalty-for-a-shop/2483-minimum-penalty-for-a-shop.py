class Solution:                                                 #     Ex:   customers = "YYNYNY"
    def bestClosingTime(self, customers: str) -> int: 
                                                                #        idx    0  1  2  3  4  5  6  7  8  9
                                                                #               –  –  –  –  –  –  –  –  –  –
                                                                #                 "Y  Y  N  N  Y  Y  Y  N  Y"

        arr = [2*(ch=='Y')-1 for ch in customers]               # <--    arr =    [1, 1,-1,-1, 1, 1, 1,-1, 1]
                                                      
        arr = list(accumulate(arr, initial = 0))                # <--    arr = [0, 1, 2, 1, 0, 1, 2, 3, 2, 3]
                                                                #                                    |     |
                                                                #                                  idx=7 idx=9
        return arr.index(max(arr))  