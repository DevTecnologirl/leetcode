class Solution:
    def reverseWords(self, s: str) -> str:
        return  ' '.join(word[::-1] for word in s.split())

entrada = "Camilly Duarte - Software Engineer"
solucao = Solution()
resultado = solucao.reverseWords(entrada)
print(resultado)  # Output: "yllimaC etaruD - erawtfoS reenignE"