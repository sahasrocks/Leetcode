class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MODULO = 10**9 + 7
        def getSeriesSum(num):
            output = (num-1)*num
            output %= MODULO
            output = output*0.5
            return int(output)
        
        y_count = defaultdict(int)

        for point in points:
            y_count[point[1]] += 1
        
        possible_pairs = []
        ttl_sum = 0
        for cord, count in y_count.items():
            series_sum = getSeriesSum(count)
            ttl_sum += series_sum
            ttl_sum %= MODULO
            possible_pairs.append(series_sum)
        
        prefix_sum = 0
        output = 0
        for count in possible_pairs:
            prefix_sum += count
            prefix_sum %= MODULO
            output += (count*(ttl_sum-prefix_sum))
            output %= MODULO
        
        return int(output)

        
        