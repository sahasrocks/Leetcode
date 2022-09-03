class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        for i in range(n):
            if i == 0:
				# leading zero is not considered
                for num in range(1, 10):
                    if num - k >= 0 or num + k < 10:
                        res.append(num)
            else:
                for _ in range(len(res)):
                    cur = res.pop(0)
                    if cur % 10 - k >= 0:
                        res.append(cur * 10 + cur % 10 - k)
					# k != 0 is to avoid the duplicated answers
                    if cur % 10 + k < 10 and k != 0:
                        res.append(cur * 10 + cur % 10 + k)
    
        return res