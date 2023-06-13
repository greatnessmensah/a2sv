class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                word1 = Counter(words[i])
                word2 = Counter(words[j])
                
                if word1.keys() == word2.keys():
                    count += 1
                    
        return count
      
      """
      Time: O(N^2)
      Space: O(1)
      """
