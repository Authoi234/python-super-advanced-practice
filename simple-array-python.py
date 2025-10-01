from array import array

nums = array("i", [1,2,3])
print(nums[0])
print(nums[1])
print(nums[2])
nums.append(5)
print(nums)
nums.remove(2)
print(nums)
print(nums.__len__())
nums.clear()
print(nums)