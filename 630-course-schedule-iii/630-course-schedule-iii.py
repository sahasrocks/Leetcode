class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        pq = []
        days = 0
        for i in range(len(courses)):
            days += courses[i][0]
            heapq.heappush(pq, (-courses[i][0], courses[i][1]))
            if days > courses[i][1]:
                days -= abs(pq[0][0])
                heapq.heappop(pq)
        return len(pq)