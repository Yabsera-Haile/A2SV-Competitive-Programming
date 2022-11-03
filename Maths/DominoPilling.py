def domino_pilling(m,n):
    domino=2*1
    board=m*n
    result=board//domino
    return result 


inputs = list(map(int, input().split()))
print(domino_pilling(inputs[0],inputs[1]))

