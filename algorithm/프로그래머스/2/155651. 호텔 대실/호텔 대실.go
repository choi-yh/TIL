import (
    "sort"
    "strconv"
    "strings"
)

func solution(book_time [][]string) int {
    bookTime := make([][]int, len(book_time))
    for i, book := range book_time {
        start, end := book[0], book[1]
        
        sSplit := strings.Split(start, ":")
        sHour, _ := strconv.Atoi(sSplit[0])
        sEnd, _ := strconv.Atoi(sSplit[1])
        
        eSplit := strings.Split(end, ":")
        eHour, _ := strconv.Atoi(eSplit[0])
        eEnd, _ := strconv.Atoi(eSplit[1])
        
        bookTime[i] = []int{60 * sHour + sEnd, 60 * eHour + eEnd + 10}
    }
    
    sort.Slice(bookTime, func(i, j int) bool { return bookTime[i][0] < bookTime[j][0] })
    
    answer := 0
    var rooms [][]int
    for _, time := range bookTime {
        var check bool
        
        for i, room := range rooms {
            if room[1] <= time[0] {
                rooms[i] = time
                check = true
                break
            }
        }
        
        if !check {
            rooms = append(rooms, time)
        }
        
        if answer < len(rooms) {
            answer = len(rooms)
        }
    }
    
    return answer
}