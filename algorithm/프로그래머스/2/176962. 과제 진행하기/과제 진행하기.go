import (
	"sort"
	"strconv"
	"strings"
)

type Plan struct {
    name string
    start int
    playtime int
}

func solution(plans [][]string) []string {
    answer := make([]string, 0, len(plans))
    sort.Slice(plans, func(i, j int) bool {return plans[i][1] < plans[j][1]})
    
    newPlan := make([]Plan, len(plans))
    for i, plan := range plans {
        startString := strings.Split(plan[1], ":")
        h, _ := strconv.Atoi(startString[0])
        m, _ := strconv.Atoi(startString[1])
        p, _ := strconv.Atoi(plan[2])
        
        newPlan[i] = Plan{
            name: plan[0],
            start: 60 * h + m,
            playtime: p,
        }
    }
    
    var q []Plan
    for i, plan := range newPlan {
        if i == len(newPlan) - 1 {
            answer = append(answer, plan.name)
            break
        }
        
        nextPlan := newPlan[i+1]
        if plan.start + plan.playtime <= nextPlan.start {
            answer = append(answer, plan.name)
            
            remainTime := nextPlan.start - (plan.start + plan.playtime)
            for len(q) > 0 && remainTime > 0 {
                holdPlan := q[len(q) - 1]
                q = q[:len(q) - 1]
                
                if holdPlan.playtime <= remainTime {
                    answer = append(answer, holdPlan.name)
                    remainTime -= holdPlan.playtime
                } else {
                    holdPlan.playtime = holdPlan.playtime - remainTime
                    remainTime = 0
                    q = append(q, holdPlan)
                }
            }
        } else {
            q = append(q, Plan{
                name: plan.name,
                start: plan.start,
                playtime: plan.start + plan.playtime - nextPlan.start,
            })
        }
    }
    
    for len(q) > 0 {
        holdPlan := q[len(q) - 1]
        q = q[:len(q) - 1]
        answer = append(answer, holdPlan.name)
    }
    
    return answer
}