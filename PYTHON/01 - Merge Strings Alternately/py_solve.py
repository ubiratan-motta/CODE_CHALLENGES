class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Append any remaining characters from both strings
        result.extend(word1[i:])
        result.extend(word2[j:])

        return ''.join(result)
        
