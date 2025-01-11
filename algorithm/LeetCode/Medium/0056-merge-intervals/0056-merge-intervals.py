class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []

        intervals.sort()
        for interval in intervals:
            while stack and stack[-1][1] >= interval[0]:
                merge = stack.pop()
                interval = [merge[0], max(merge[1], interval[1])]

            stack.append(interval)

        return stack