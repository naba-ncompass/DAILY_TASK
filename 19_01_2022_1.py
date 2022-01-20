print("WORLD OF ENGLISH")

A = input("enter the STRING :")

upper, lower = 0, 0

for i in range(len(A)):
    if A[i].isupper():
        upper += 1
    elif A[i].islower():
        lower += 1

# print('Upper case letters:', upper)
# print('Lower case letters:', lower)

if len(A)/2 < upper:
   print(A.upper())
elif len(A)/2 <= lower:   
   print(A.lower())


