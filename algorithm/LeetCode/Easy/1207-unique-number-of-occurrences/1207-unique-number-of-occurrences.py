class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = {i:0 for i in range(-1000, 1001)}
        for num in arr:
            count_dict[num] += 1

        answer_check_arr = [True] * 2001
        for v in count_dict.values():
            if v == 0:
                continue

            if answer_check_arr[v] is False:
                return False
            
            answer_check_arr[v] = False

        return True