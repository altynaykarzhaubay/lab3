N = int(input("N = "))
sum1 = N
sum2 = 0
for i in range(1, N):
    sum1 += i
    sum2 += int(input())
print(sum1 - sum2)