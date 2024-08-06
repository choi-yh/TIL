def getTime(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def getMusicList(m):
    arr = []
    for i in range(len(m) - 1):
        if m[i] == "#":
            continue
        
        if m[i + 1] == "#":
            arr.append(m[i: i+2])
        else:
            arr.append(m[i])
    
    if m[-1] != "#":
        arr.append(m[-1])
        
    return arr

def check(m, music):
    if len(m) > len(music):
        return False
    
    for i in range(len(music)):
        if music[i] == m[0]:
            flag = True
            for j in range(len(m)):
                if i + j >= len(music):
                    flag = False
                    break
                
                if music[i+j] != m[j]:
                    flag = False
                    break
            
            if flag:
                return True
    
    return False

def solution(m, musicinfos):
    answer = "(None)"
    answer_time = 0
    
    m_arr = getMusicList(m)
    
    for musicinfo in musicinfos:
        start, end, name, music = musicinfo.split(",")
        play_time = getTime(end) - getTime(start)
        
        music_arr = getMusicList(music)
        
        if len(music_arr) >= play_time:
            check_arr = music_arr[:play_time]
        else:
            play = music_arr * (play_time // len(music_arr) + 1)
            check_arr = play[:play_time * (play_time // len(music_arr))]
        
        if check(m_arr, check_arr) and play_time > answer_time:
            answer = name
            answer_time = play_time
    
    return answer
