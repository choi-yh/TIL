import (
    "math"
)

func solution(r1 int, r2 int) int64 {
    var count int64 = 0
    for i := 0; i <= r2; i++ {
        y1 := int64(math.Ceil(math.Sqrt(float64(r1 * r1 - i * i))))
        if i > r1 {
            y1 = 0
        }
        
        y2 := int64(math.Floor(math.Sqrt(float64(r2 * r2 - i * i))))
        
        count += y2 - y1 + 1
    }
    
    return 4 * count - int64((r2 - r1 + 1) * 4)
}