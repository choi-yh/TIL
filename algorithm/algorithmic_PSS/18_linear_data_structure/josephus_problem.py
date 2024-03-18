# https://www.acmicpc.net/problem/1158

n, k = map(int, input().split())
# n, k = 7, 3

array = [i for i in range(1, n+1)]
answer = []

pop_index = 0
while len(array) > 0:
   pop_index = (pop_index + k - 1) % len(array)
   answer.append(str(array.pop(pop_index)))
    
josephus = '<' + ', '.join(answer) + '>'
print(josephus)
