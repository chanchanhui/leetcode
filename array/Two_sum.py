class Solution(object):
	def twoSum1(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		print(len(nums))
		for i in range(len(nums)-1):
			print(i)
			temp_val=target-nums[i]
			for j in range(i+1,len(nums),1):
				if temp_val==nums[j]:
					return [i,j]
#trading space for speed
	def twoSum2(self, nums, target):
		l = {}
		for i in range(len(nums)):
			l[nums[i]]=i
		for i in range(len(nums)):
			if (target-nums[i] in l) and (l[target-nums[i]]!=i):
				return [i,l[target-nums[i]]]
	def twoSum3(self, nums, target):
		l = {}
		for i in range(len(nums)):
			tmp_val=target- nums[i]
			if tmp_val in l:
				return [i,l[tmp_val]]
			else:
				l[nums[i]]=i


TEST=Solution()
list1=[3,2,4]

print(TEST.twoSum1(list1,6))
print(TEST.twoSum2(list1,6))
print(TEST.twoSum3(list1,6))