# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0
#         nei=collections.defaultdict(list)
#         wordList.append(beginWord)
#         for word in wordList:
#             for j in range(len(word)):
#                 pattern = word[:j] + '*' + word[j+1:]
#                 nei[pattern].append(word)
#         visit=set([beginWord])
#         q=deque([beginWord])
#         res=1
#         while q:
#             word=q.popleft()
#             if word==endWord:
#                 return res
#             for j in range(len(word)):
#                 pattern = word[:j] + '*' + word[j+1:]  
#                 for neiWord in nei[pattern]:
#                     if neiWord not in visit:
#                         visit.add(neiWord)
#                         q.append(neiWord)
#             res+=1            
#         return 0                 
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)

        # Build pattern → word map
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1  # Level count (number of transformations)

        while q:
            for _ in range(len(q)):  # process current level
                word = q.popleft()
                if word == endWord:  # ✅ correct check
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1  # ✅ increment after finishing one level

        return 0
