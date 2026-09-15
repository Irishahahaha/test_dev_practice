score=85
if score<60:
    print("不及格")
elif 60<=score<90:
    print("及格")
else:print("优秀")

for i in range(5):
    print(i,end='')
print()
count=0
while count<3:
    print(count+1)
    count=count+1
nums=[1,2,3,4,5,6,7,8,9]
nums.append(2) #末尾加一个
nums.remove(1) #删掉第一个1
nums.sort()

print("排序后：",nums)
print("最大值：",max(nums))
print("平均值",sum(nums)/len(nums))

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    result=[i,j]
                    return result
nums=[2,7,11,15]
target=9
sol=Solution()
ans=sol.twoSum(nums,target)
print(ans)

