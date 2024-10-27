class Solution:
    def __init__(self):
        self.palindromes = []

    def partition(self, s: str) -> List[List[str]]:
        self.get_palindromes_partitioning(list(s), [])
        return self.palindromes

    def get_palindromes_partitioning(self, l: List[str], partition: List[str]):
        if len(l) == 0:
            self.palindromes.append(partition[:])
            return

        for i in range(1, len(l) + 1):
            if self.is_palindrome(l[:i]):
                partition.append("".join(l[:i]))

                self.get_palindromes_partitioning(l[i:], partition)

                partition.pop()

    def is_palindrome(self, l: List[str]) -> bool:
        n = len(l)
        mid = n // 2

        if n % 2 == 0:
            return l[:mid] == l[mid:][::-1]
        else:
            return l[: mid + 1] == l[mid:][::-1]
