## Subsets 

class Solution:

	def subsets(self,nums):
		res = []
		self.dfs2(0,nums,res,[])
		return res 

	def dfs2(self,index,nums, res, path):

		res.append(list(path))

		if index == len(nums):
			return 

		for i in range(index,len(nums)):
			path.append(nums[i])
			self.dfs2(i+1,nums,res,path)
			path.pop()


