class Solution:
    def reverseWords(self, s: str) -> str:
        palavras_invertidas = s[::-1]
        frase_invertida = palavras_invertidas.split()
        frase_original = frase_invertida[::-1]
        return " ".join(frase_original)