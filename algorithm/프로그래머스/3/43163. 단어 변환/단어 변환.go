func isChangable(src, dst string) bool {
    cnt := 0
    for i, _ := range src {
        if src[i] != dst[i] {
            cnt += 1
        }
    }
    
    return cnt == 1
}

func solution(begin string, target string, words []string) int {
    dist := make(map[string]int, len(words) + 1)
    for _, word := range words {
        dist[word] = 999
    }
    dist[begin] = 0
    
    q := []string{begin}
    for len(q) > 0 {
        w := q[0]
        q = q[1:]
        
        if w == target {
            return dist[w]
        }
        
        for _, word := range words {
            if isChangable(w, word) && dist[word] > dist[w] {
                q = append(q, word)
                dist[word] = dist[w] + 1
            }
        }
    }
    
    return 0
}