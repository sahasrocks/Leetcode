class Solution:
    def canConstruct(self, ran: str, mag: str) -> bool:
        mag = list(mag)
        for i in ran:
            if i in mag:
                mag.remove(i)
            else :
                return False
        return True    