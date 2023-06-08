class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {char: index for index, char in enumerate(order)}
        
        word = [[alien_dict[cha] for cha in char] for char in words]
        
        for word1, word2 in zip(word, word[1:]):
            if word1 > word2:
                return False
        return True   
