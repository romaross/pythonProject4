list1 = [1, 2, 3, 4, 5]
tmp1 = list1[0]
for i in range(1, len(list1)):
    list1[i-1] = list1[i]
list1[len(list1)-1] = tmp1
print('shifted to left:', list1)