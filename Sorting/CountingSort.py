def countingSort(n, arr):
    freq = [0]*100
    for num in range(0, n):
        temp = arr[num]
        freq[temp] += 1
    return freq
