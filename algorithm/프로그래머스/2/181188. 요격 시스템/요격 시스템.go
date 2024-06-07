import (
    "sort"
)

func solution(targets [][]int) int {
    answer := 0
    
    // targets[i][1] 오름차순 정렬
    sortedTargets := make([][]int, len(targets))
    copy(sortedTargets, targets)
    sort.Slice(sortedTargets, func(i, j int) bool { return sortedTargets[i][1] < sortedTargets[j][1] })
    
    // 탐색해가면서 sortedTargets 의 s 가 end 보다 작으면 이미 체크가 된 것.
    // 새로운 s 가 end 보다 큰 경우에만 answer 증가 후 end 갱신
    end := 0
    for _, target := range sortedTargets {
        if target[0] >= end {
            answer += 1
            end = target[1]
        }
    }
    
    return answer
}