import "sort"

func solution(sequence []int, k int) []int {
    if sequence[0] == k {
        return []int{0, 0}
    }
    
    candidates := getCandidates(sequence, k)
    sort.Slice(candidates, func(i, j int) bool {
        return candidates[i][1] - candidates[i][0] < candidates[j][1] - candidates[j][0]
    })
    
    return candidates[0]
}

func getCandidates(sequence []int, k int) [][]int {
    candidates := [][]int{}
    
    start, end := 0, 1
    subSeqSum := sequence[0] + sequence[1]
    for start <= end {
        if subSeqSum == k {
            candidates = append(candidates, []int{start, end})
        }
        
        if subSeqSum > k || end == len(sequence) - 1 {
            subSeqSum -= sequence[start]
            start += 1
        } else {
            end += 1
            subSeqSum += sequence[end]
        }
    }
    
    return candidates
}
