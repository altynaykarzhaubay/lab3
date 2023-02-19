A=int(input("A = "))
B=int(input("B = "))
if A<B:
    for i in range(A, B+1):
        print(A)
        A+=1
else:
    for i in range(B-1, A):
        print(A)
        A-=1