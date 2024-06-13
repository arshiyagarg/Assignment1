lst = [3, 4, 7, 8, 9]
mini = lst[0]
maxi = lst[0]

for i in range(1, len(lst)):
    if mini > lst[i] :
        mini = lst[i]
    if maxi < lst[i]:
        maxi = lst[i]

print("Minimum Value: ", mini)
print("Maximum Value: ", maxi)