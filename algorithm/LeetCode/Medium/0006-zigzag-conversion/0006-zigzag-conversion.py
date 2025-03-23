class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        rows = [[] for _ in range(numRows)]
        
        flags = ["DOWN", "UP"]
        
        row_idx = 0
        flag = "DOWN"
        for i in range(n):
            rows[row_idx].append(s[i])

            if flag == "DOWN":
                row_idx += 1
            elif flag == "UP":
                row_idx -= 1

            if row_idx == numRows - 1:
                flag = "UP"
            elif row_idx == 0:
                flag = "DOWN"

        return ''.join([''.join(row) for row in rows])
