import "sort"

func getMineralGroups(minerals []string) [][]int {
    mineralGroups := make([][]int, len(minerals) / 5 + 1)
    for i := 0; i < len(minerals) / 5 + 1; i++ {
        mineralGroups[i] = make([]int, 3)
        
        target := make([]string, 5)
        if 5 * i + 5 > len(minerals) {
            target = minerals[5*i:]
        } else {
            target = minerals[5 * i: 5 * i + 5]
        }
        
        for _, mineral := range target {
            switch mineral {
            case "diamond":
                mineralGroups[i][0] += 1
            case "iron":
                mineralGroups[i][1] += 1
            case "stone":
                mineralGroups[i][2] += 1    
            }
        }
    }
    
    return mineralGroups
}

func getFatigue(picksMap map[string]int, mineralGroups [][]int) int {
    var fatigue int
    
    for _, mineralGroup := range mineralGroups {
        pick := "stone"
        if picksMap["iron"] > 0 {
            pick = "iron"
        }
        if picksMap["diamond"] > 0 {
            pick = "diamond"
        }
        
        switch pick {
        case "diamond":
            fatigue += mineralGroup[0] + mineralGroup[1] + mineralGroup[2]
        case "iron": 
            fatigue += 5 * mineralGroup[0] + mineralGroup[1] + mineralGroup[2]
        case "stone":
            fatigue += 25 * mineralGroup[0] + 5 * mineralGroup[1] + mineralGroup[2]
        }
        
        picksMap[pick]--
    }
    
    return fatigue
}

func solution(picks []int, minerals []string) int {
    picksCount := 5 * (picks[0] + picks[1] + picks[2])
    if len(minerals) > picksCount {
        minerals = minerals[:picksCount]
    }
    
    mineralGroups := getMineralGroups(minerals)
    
    sort.Slice(mineralGroups, func(i, j int) bool {
        if mineralGroups[i][0] == mineralGroups[j][0]{
            return mineralGroups[i][1] > mineralGroups[j][1]
        }
        
        return mineralGroups[i][0] > mineralGroups[j][0]
    })
    
    picksMap := map[string]int{
        "diamond": picks[0],
        "iron": picks[1],
        "stone": picks[2],
    }
    
    answer := getFatigue(picksMap, mineralGroups)
    
    return answer
}