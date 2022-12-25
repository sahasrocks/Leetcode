class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = [0] * len(queries)
        for id, query in enumerate(queries):
            spec_sum = 0
            for i, number in enumerate(sorted(nums)):
                spec_sum += number

                if spec_sum <= query:
                    answer[id] += 1
                else:
                    break

        return answer