import random
nums= []
def find_missing_nums(nums):
    n= int(input())
    for i in range(n):
        I = random.randint(1, n)
        nums.append(I)
    nums1= []
    for i in range(1,n+1):
        nums1.append(i)
    a=set(nums1)
    b=set(nums)
    res = [x for x in nums1 + nums if x not in nums1 or x not in nums]
    return(res)
print(find_missing_nums(nums))

