class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap keys = frequency list 
        #values = list of strings that have identical frequency list
        
        res = defaultdict(list) #makes hashmap of lists
        for string in strs:
            freqList = [0] * 26
            for character in string:
                freqList[ord(character) - ord('a')] += 1
            res[tuple(freqList)].append(string)
        return list(res.values())


        