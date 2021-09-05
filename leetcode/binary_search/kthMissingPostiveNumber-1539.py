class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        if not arr or k == 0:
            return 
        
        ret = [i for i in range(1,arr[0])] ## ret 先存储第一个数之前的数，如果没有就为空
        
        for index in range(len(arr)-1):
            
            if len(ret) >= k:  ## [2,3,4,7,11], k = 5，ret = [1,5,6,8,9,10,12,13,...],那么就取ret 的第k-1个
                return [k-1]
            
            l = arr[index]  ## left = 第一个index
            r = arr[index+1] ## right = 第一个index + 1
            for i in range(l+1,r): ## 检查这个区间里是否有missing value， 如果有append
                ret.append(i)
            
        ## 现在ret 是一个含有全部mssing value的数组
        
        length = len(ret)
        base = arr[-1]
        
        ## 现在考虑[1,2,3,4], k = 2 这种没有mssing 的情况
        ## 如果len(ret) 比k 小，则取最后一个数为base，然后+1 append 直到length 和k一样大
        while (length < k):
            base += 1
            ret.append(base)
            length += 1
        
        ## 返回最后一个数
        return ret[k-1]
            