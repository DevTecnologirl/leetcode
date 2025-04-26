class Solution:
    def maximumLengthSubstring(self, s:str) -> int:
        l, r = 0, 0 #ponteiro esq e direi
        _max = 1
        counter = {} 

        counter[s[0]] = 1
        while r < len(s) -1:
            r+=1
            if counter.get(s[r]):
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1
            while counter[s[r]] == 3:
                counter[s[l]] -= 1
                l += 1
            _max = max(_max, r - l + 1)
        return _max
# Teste com a string "abcabcabc"
s = "abcabcabc"
solucao = Solution()
resultado = solucao.maximumLengthSubstring(s)
print(resultado)  # Output: 3 (a substring "abc" tem comprimento 3)