import numpy as ap
# arr = ap.array([2, 4, 6, 8, 10])
# print(str.format("新建的数组为：{0}", arr))
# print(arr.dtype)
# print(arr.shape)
# print(arr.size)
# arr = ap.arange(1, 7)
# print(arr)
# arr1 = ap.zeros(5)
# arr1 = arr1.astype(ap.int32)
# print(arr1)
# arr2 = ap.ones((5, 5))
# print(arr2)
# arr3 = ap.empty((3, 3))
# print(arr3)
# arr = ap.eye(4, dtype=ap.int, k=-2)
# print(arr)
# # arr3 = ap.linspace(0, 10, 15)
# # print(arr3)
# arr4 = ap.logspace(0, 1, 5)
# print(arr4)
# arr = ap.random.rand(2, 3, 5)
# print(arr)
# arr = ap.arange(0, 10, 2)
# print(arr)
# ap.random.shuffle(arr)
# print(arr)
# arr = ap.random.choice(arr, 3)
# print(arr)
# arr = ap.arange(16)
# print(arr)
# arr.shape = 4, 4
# print(arr.flatten("F"))
# arr = arr.reshape(2, 8)
# print(arr.T)
# arr1 = ap.arange(9).reshape(3, 3)
# print(arr1)
# arr2 = ap.eye(3, 4)
# print(arr2)
# arr3 = ap.hstack((arr1, arr2))
# print(arr3)
# # arr2 = arr2.reshape(4, 3)
# # print(arr2)
# arr4 = ap.vstack((arr1, arr2.T))
# print(arr4)
# arr = ap.random.randint(0, 16, 10)
# print(arr)
# print(ap.tile(arr, 2))
# arr = ap.array([[4, 3, 2], [2, 1, 4]])
# arr.sort(axis=0)
# print(arr)
# numeric_strings = ap.array(['1.7', '-9.6', '42'], dtype=ap.string_)
# numeric_strings.astype(float)
# print(numeric_strings)
# arr = ap.arange(10, 1, -1)
# arr[2] = 33
# print(arr)
# arr = ap.arange(10)
# arr[5:8] = 12
# print(arr)
arr = ap.arange(10)
arr_slice = arr[3:8]
arr_slice[1::2] = 12
print(arr_slice)










