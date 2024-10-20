class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0

        while left < right:
            if height[left] <= height[right]:
                left_max = max(height[left], left_max)
                # if height[left] < left_max:
                answer += left_max - height[left]
                left += 1
            else:
                right_max = max(height[right], right_max)
                # if height[right] < right_max:
                answer += right_max - height[right]
                right -= 1

        return answer
