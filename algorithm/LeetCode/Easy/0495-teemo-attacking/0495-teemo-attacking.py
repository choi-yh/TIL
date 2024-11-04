class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned_time = 0

        poison_end_time = 0
        for time in timeSeries:
            if time >= poison_end_time:
                poisoned_time += duration
            else:
                poisoned_time += duration - (poison_end_time - time)

            poison_end_time = time + duration

        return poisoned_time