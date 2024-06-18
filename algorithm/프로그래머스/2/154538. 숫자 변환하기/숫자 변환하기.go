var maxInt = 1000001

func solution(x int, y int, n int) int {
    counts := make([]int, y + 1)
    for i := 0; i < y + 1; i++ {
        counts[i] = maxInt
    }
    counts[x] = 0
    
    var q []int
    q = append(q, x)
    
    for len(q) > 0 {
        v := q[0]
        q = q[1:]
        
        p := v + n
        d := v * 2
        t := v * 3
        
        if p < y + 1 && counts[v] + 1 < counts[p] {
            counts[p] = counts[v] + 1
            q = append(q, p)
        }
        
        if d < y + 1 && counts[v] + 1 < counts[d]  {
            counts[d] = counts[v] + 1
            q = append(q, d)
        }
        
        if t < y + 1 && counts[v] + 1 < counts[t]  {
            counts[t] = counts[v] + 1
            q = append(q, t)
        }
    }
    
    if counts[y] == maxInt {
        return -1
    }
    
    return counts[y]
}