import numpy as np

arr = np.array(
    [1, 2, 4]
)

print(arr,type(arr))  # 1 * 3 matrix
print("shape of array: ", arr.shape)  #it returns a tuple

arr2D = np.array([
    [2, 3],
    [5, 6],
    [7,8]
])

print(arr2D, arr2D.shape)  #tuple of no of rows and no of coloumn

print(arr[0], arr[1], arr[2])

print(
    arr2D[0,0], arr2D[0,1]
)

print(
    arr2D[1,0], arr2D[1,1]
)

print(
    arr2D[2,0], arr2D[2,1]
)

arr3D = np.array([
    [
        [1, 2, 3],
        [3, 4, 5],
    ],
    [
        [6, 7, 8],
        [9, 10, 11],
    ],
    [
        [12, 13, 14],
        [15, 16, 17],
    ]

])

print(arr3D)
print(arr3D[0])
print(arr3D[0,0])
print(arr3D[0,0,1])

arr2D[0] = [4, 5]
print(arr2D)
arr2D[0,0] = 7
print(arr2D)

zeros = np.zeros([4,5])
print(zeros)
print(zeros.dtype)

ones = np.ones([3, 3])
print(ones)

ones = np.ones([3,])
print(ones)
print(ones.dtype)

consts = np.full([])