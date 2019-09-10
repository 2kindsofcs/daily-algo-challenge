class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainDic = {}
        for chunk in cpdomains:
            tempList = chunk.split()
            count = int(tempList[0])
            address = tempList[1]
            index = 0
            while index >= 0:
                if address in domainDic:
                    domainDic[address] += count
                else:
                    domainDic[address] = count
                index = address.find('.')
                address = address[(index + 1):]
        keyList = domainDic.keys()
        result = []
        for key in keyList:
            output = str(domainDic[key]) + " " + key
            result.append(output)
        return result
    
# Runtime: 60 ms, faster than 87.53% of Python3 online submissions for Subdomain Visit Count.
# Memory Usage: 13.8 MB, less than 8.33% of Python3 online submissions for Subdomain Visit Count.
