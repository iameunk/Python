n = int(input())
nums = []

for _ in range(n) :
    nums.append(int(input()))

for i in range(len(nums)-1) :
    for j in range(len(nums)-i-1) :
        if nums[j] > nums[j+1] :
            nums[i], nums[j] = nums[j], nums[i]

for k in nums :
    print(k)
