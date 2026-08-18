class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dicto = {}

        for char in magazine:
            dicto[char] = dicto.get(char,0) + 1

        for chars in ransomNote:
            dicto[chars] = dicto.get(chars,0) - 1
            
            if dicto[chars] < 0:
                return False
        return True