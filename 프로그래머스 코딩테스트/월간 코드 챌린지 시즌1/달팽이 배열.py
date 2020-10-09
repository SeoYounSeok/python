def solution(n):
    answer = []
    arr = [[0 for j in range(n)] for i in range(n)] #1
    row = 0 #2
    col = -1 #2
    cnt = 1 #3
    trans = 1 #4
    while n > 0: #5
        for i in range(n): #6
            col += trans
            arr[row][col] = cnt
            cnt += 1
        n -= 1 #7
        for j in range(n): #8
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1 #9
    
    print(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            answer.append(arr[i][j])
    print(answer)
    return 1
