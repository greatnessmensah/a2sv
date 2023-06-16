class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first_letters = set(words[0])

        common_letters = []
        for letter in first_letters:
            count = min(word.count(letter) for word in words)
            common_letters.extend([letter] * count)

        return common_letters
    
    
    """
    Time: O(N*M)
    Space: O(N)
    """
    
