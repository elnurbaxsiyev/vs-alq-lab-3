import random

def printList(lst):
    for row in lst:
        for element in row:
            print(element, end='   ')
        print()

n = int(input("setir sutun sayini daxil edin:"))
a = []

for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(random.randint(-9, 9))

print(" Matris:")
printList(a)
print()

total_sum = 0

for i in range(n):
    for j in range(i+1, n):
        if a[i][j] > 0:
            total_sum += a[i][j]

print("Baş diagonalin üstündeki pozitif elemanların toplamı:", total_sum)
