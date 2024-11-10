class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def sol(idx: int, expression: str, last_value: str):
            if idx == len(num) - 1:
                if eval(expression) == target:
                    answer.append(expression)
                return

            next_idx = idx + 1
            next_num = num[next_idx]

            sol(next_idx, expression + "+" + next_num, next_num)
            sol(next_idx, expression + "-" + next_num, next_num)
            sol(next_idx, expression + "*" + next_num, next_num)

            if last_value != "0":
                sol(next_idx, expression + next_num, last_value + next_num)

        answer = []
        sol(0, num[0], num[0])
        return answer
