class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sortednums = sorted(nums)[::-1]
        retlist = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums)+1))
        mydict = {num: result for num, result in zip(sortednums, retlist)}
        return map(mydict.get, nums)
    
    
    '''
    - redo [ ]
    - list comprehension + map + zip 
    '''