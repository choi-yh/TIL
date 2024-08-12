def rotate(grid, query):
    values = []
    
    x1, y1, x2, y2 = query
    lu, ru, ld, rd = grid[x1 - 1][y1 - 1], grid[x1 - 1][y2 - 1], grid[x2 - 1][y1 - 1], grid[x2 - 1][y2 - 1]
    
    target = list(map(list, grid))
    for i in range(x1 - 1, x2):
        if i == x1 - 1:
            for j in range(y1 - 1, y2):
                if j == y1 - 1:
                    target[i][j] = grid[i + 1][j]
                else:
                    target[i][j] = grid[i][j - 1]
                    
                values.append(target[i][j])
        elif i == x2 - 1:
            for j in range(y1 - 1, y2):
                if j == y2 - 1:
                    target[i][j] = grid[i - 1][j]
                else:
                    target[i][j] = grid[i][j + 1]
                
                values.append(target[i][j])
        else:
            target[i][y1 - 1] = grid[i + 1][y1 - 1]
            target[i][y2 - 1] = grid[i - 1][y2 - 1]
            
            values.append(target[i][y1 - 1])
            values.append(target[i][y2 - 1])
    
    return target, min(values)

def solution(rows, columns, queries):
    answer = []
    
    grid = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    for query in queries:
        grid, min_value = rotate(grid, query)
        
        answer.append(min_value)
    
    return answer