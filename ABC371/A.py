input = input().split()
A = 0
B = 0
C = 0
if input[0] == ">":
    A = A + 1
else:
    B = B + 1

if input[1] == ">":
    A = A + 1
else:
    C = C + 1

if input[2] == ">":
    B = B + 1
else:
    C = C + 1

order = []
order.append(A)
order.append(B)
order.append(C)
order.sort()
if order[1]==A:
    print("A")
if order[1]==B:
    print("B")
if order[1]==C:
    print("C")