class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cum_alt = [0]
        for i in range(len(gain)):
            cum_alt.append(cum_alt[i] + gain[i])

        return max(cum_alt)