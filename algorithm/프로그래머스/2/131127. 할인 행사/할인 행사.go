func compare(want map[string]int, target map[string]int) bool {
    for k, v := range want {
        if target[k] != v {
            return false
        }  
    }
    
    return true
}

func solution(want []string, number []int, discount []string) int {
    wantMap := make(map[string]int, len(want))
    for i, v := range want {
        wantMap[v] = number[i]
    }
    
    checkMap := make(map[string]int, 10)
    for _, v := range discount[:10] {
        checkMap[v] += 1
    }
    
    answer := 0
    if compare(wantMap, checkMap) {
        answer += 1
    }
    
    for i := 1; i < len(discount) - 9; i++ {
        checkMap[discount[i-1]]--
        checkMap[discount[i+9]]++
        
        if compare(wantMap, checkMap) {
            answer++
        }
    }
    
    return answer
}