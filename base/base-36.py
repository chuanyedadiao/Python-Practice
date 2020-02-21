def printArray(arr):
    for i in range(len(arr)):
        print(arr[i],end=' ')


d = int(input('请输入d'))
arr1 = [1,2,3,4,5,6,7]
arr2 = arr1[:d]

for i in range(d,len(arr1)):
    arr1[i-d] = arr1[i]

for i in range(d):
    arr1[len(arr1)-d+i] = arr2[i]

printArray(arr1)
