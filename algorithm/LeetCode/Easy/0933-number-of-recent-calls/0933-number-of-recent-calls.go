type RecentCounter struct {
    queue []int
}


func Constructor() RecentCounter {
    return RecentCounter{
        queue: []int{},
    }
}


func (this *RecentCounter) Ping(t int) int {
    targetIdx := 0
    for i := 0; i < len(this.queue); i++ {
        if len(this.queue) == 0 {
            break
        }

        if this.queue[i] >= t - 3000 {
            targetIdx = i
            break
        }
    }

    this.queue = this.queue[targetIdx:]    
    this.queue = append(this.queue, t)

    return len(this.queue)
}