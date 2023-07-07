class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ms = k
        count = collections.Counter(answerKey[:k]) #k is taken as the size of window
        left = 0
        for right in range(k,len(answerKey)):
            count[answerKey[right]] += 1

            while min(count['T'],count['F'])>k:
                count[answerKey[left]] -= 1
                left += 1
            ms = max(ms , right-left+1)
        return ms