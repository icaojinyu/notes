"""
# type(obj) 输出obj的类型
# len(obj) 输出obj的长度
# 可以通过索引访问list的中的数据
# 索引可以为负数,最大值为len - 1,但索引不能越界
# list.append(el) 在末尾追加元素
# list.insert(index) 在指定索引位置插入元素
# list.pop(index) 删除指定位置的元素,如果不传index,默认删除末尾的元素
"""

arr = [1, 2, 3, 4, 'hello', True]

print(type(arr))  # <class 'list'>

print(len(arr))  # 6

print(arr[0])
print(arr[1])
print(arr[-1])  # True
print(arr[-2])  # hello

# 追加
arr.append('追加的元素')
print(arr)

# 插入
arr.insert(-2, '插入的元素')
print(arr)

# 删除list末尾的元素
res = arr.pop()
print(res)
print(arr)
