def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    
    arr2_transpose = [[] for _ in range(len(arr2[0]))]
    for i in range(len(arr2)):
        for j in range(len(arr2[i])):
            arr2_transpose[j].append(arr2[i][j])

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            element = 0
            for k in range(len(arr1[i])):
                element += arr1[i][k] * arr2[k][j]
            answer[i].append(element)

    return answer
