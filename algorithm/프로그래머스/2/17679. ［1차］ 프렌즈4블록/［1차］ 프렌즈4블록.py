def get_4_blocks(m, n, grid):
    cnt = 0
    check = [[0] * n for _ in range(m)]
        
    for i in range(m):
        for j in range(n):
            block = grid[i][j]
            target = [(i + 1, j), (i, j + 1), (i + 1, j + 1)]
            
            flag = True
            for x, y in target:
                if x >= m or y >= n or grid[x][y] != block or grid[x][y] == -1:
                    flag = False
                    break
            
            if flag:
                cnt += 1
                check[i][j] = 1
                for x, y in target:
                    check[x][y] = 1
                    
    return check

def get_block_cnt(m, n, check):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if check[i][j] == 1:
                cnt += 1
    
    return cnt

def move_blocks(m, n, grid, check):
    for i in range(m):
        for j in range(n):
            if check[i][j] == 1:
                grid[i][j] = -1
                
    moved_grid = []
    for j in range(n):
        col = [grid[i][j] for i in range(m)]
        
        move_dist = col.count(-1)
        moved_col = [-1] * move_dist
        for e in col:
            if e != -1:
                moved_col.append(e)
        
        moved_grid.append(moved_col)
        
    moved_grid_trans = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            moved_grid_trans[i][j] = moved_grid[j][i]
    
    return moved_grid_trans

def solution(m, n, board):
    answer = 0
    
    grid = [list(row) for row in board]
    while True:
        check = get_4_blocks(m, n, grid)
        cnt = get_block_cnt(m, n, check)
        if cnt == 0:
            return answer

        grid = move_blocks(m, n, grid, check)
        answer += cnt
        
    return answer