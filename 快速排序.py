#快速排序

def showData(data):
    size=len(data)
    for i in range(size):
        print(str(data[i])+',',end=' ')

def quick_sort(data,size,left,right):
    #快速排序的关键步骤
    if left<right:
        left_idx=left+1
        while data[left_idx]<data[left]:
            if left_idx+1>size:
                break
            left_idx+=1

        right_idx=right
        while data[right_idx]>data[left]:
            right_idx-=1

        while left_idx<right_idx:
            data[left_idx],data[right_idx]=data[right_idx],data[left_idx]

            left_idx+=1
            while data[left_idx]<data[left]:
                left_idx+=1

            right_idx-=1
            while data[right_idx]>data[left]:
                right_idx-=1

        data[left],data[right_idx]=data[right_idx],data[left]

        print("第n次排序的结果是：",end='')
        for i in range(size):
            print(str(data[i])+",",end='')
        print()

        quick_sort(data,size,left,right_idx-1)
        quick_sort(data,size,right_idx+1,right)


def main():
    data=[0]*100
    data=[3,6,8,9,1,2,4,0,7,5]
    quick_sort(data,10,0,9)
    print("排序结果为：",end='')
    showData(data)

main()
"""
# 快速排序练习

import random


# 产生随机数
def inputarr(data, size):
    for i in range(size):
        data[i] = random.randint(1, 100)


# 打印列表
def showdata(data):
    for value in data:
        print(str(value) + ",", end=' ')

    print()


# 快速排序的关键步骤
def quick_sort(data, size, left, right):
    if left < right:
        left_idx = left + 1
        while data[left_idx] < data[left]:
            if left_idx + 1 > size:
                break
            left_idx += 1

        right_idx = right
        while data[right_idx] > data[left]:
            right_idx -= 1

        while left_idx < right_idx:
            data[left_idx], data[right_idx] = data[right_idx], data[left_idx]

            left_idx += 1
            while data[left_idx] < data[left]:
                left_idx += 1

            right_idx -= 1
            while data[right_idx] > data[left]:
                right_idx -= 1

        data[left], data[right_idx] = data[right_idx], data[left]

        for value in data:
            print(str(value) + ",", end=" ")
        print()

        quick_sort(data, size, left, right_idx - 1)
        quick_sort(data, size, right_idx + 1, right)


def main():
    data = [0] * 100
    size = int(input("请输入数组的长度："))
    data=[3,6,8,9,1,2,4,0,7,5]
    print("未排序的原始数据为：")
    showdata(data)
    print("排序的过程为：")
    quick_sort(data, size, 0, size - 1)
    print("最后排序完成后的结果为：")
    showdata(data)


main()
"""


def twoSum(nums, target):
    lens = len(nums)
    j=-1
    for i in range(lens):
        if (target - nums[i]) in nums:
            if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                continue
            else:
                j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2
                break
    if j>0:
        return [i,j]
    else:
        return []
