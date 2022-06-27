M = int(input("輸入階乘值M:"))
O = 1
N = 1

while (O < M):
    O = O*N
    N = N + 1
print("超過M為",M,"的最小階層N值為:",N-1)