import sortedcontainers


# T: O(n*log(n))
# S: O(n)
class MyCalendar:
    def __init__(self):
        self.events = sortedcontainers.SortedList()

    def book(self, start: int, end: int) -> bool:
        if start >= end:
            return False

	    # case 2, 3
        i = self.events.bisect_right((start,))
        if i > 0:
            _, is_end = self.events[i - 1]
            if not is_end:
                return False

        # case 1
        i = self.events.bisect_right((end - 1, True))
        if i > 0:
            time, is_end = self.events[i - 1]
            if not is_end or start <= time:
                return False

        self.events.add((start, False))
        self.events.add((end - 1, True))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)