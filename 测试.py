"""
a=[]
b=int(input())

for i in range(b):
    a.append(int(input()))

sum=0

for i in range(len(a)):
    sum+=a[i]*10*(b-1)
    sum+=a[i]*(b-1)

print(sum,end='')



a=[]
a=input().split()

x=a[0]
sum=0

for i in range(1,len(a)):
    sum+=a[i]*10*(x-1)
    sum+=a[i]*(x-1)

print(sum,end='')
"""


class Solution:
    def twoSum(self, nums, target):
        # 设置两个下标的变量
        for i1 in range(len(nums)):
            i2 = i1 + 1
            while nums[i1] + nums[i2] != target:
                i2 += 1

        a = []
        a.append(i1)
        a.append(i2)

        print(a)

        return a

nums=[2,7,11,15]
a=9
s=Solution()
s.twoSum(nums,a)
