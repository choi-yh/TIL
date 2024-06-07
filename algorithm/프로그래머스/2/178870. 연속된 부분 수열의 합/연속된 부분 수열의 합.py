def solution(sequence, k):
    if sequence[0] == k:
        return [0, 0]
    
    candidates = []
    
    start, end = 0, 1
    subSeqSum = sequence[0] + sequence[1]
    while start <= end:
        if subSeqSum == k:
            candidates.append([start, end])
        
        if subSeqSum > k or end == len(sequence) - 1:
            subSeqSum -= sequence[start]
            start += 1
        else:
            end += 1
            subSeqSum += sequence[end]
    
    sortedCandidates = sorted(candidates, key = lambda x : x[1] - x[0])
    
    return sortedCandidates[0]