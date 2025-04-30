def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complemento = target - num
        if complemento in seen:
            return [seen[complemento], i]
        seen[num] = i
    return []

#seen é um dicionário: {número: índice}
# Para cada número:
# Calculamos o complemento = target - num
# Se o complemento já estiver em seen, retornamos os dois índices
# Caso contrário, guardamos num no dicionário
print(twoSum([2, 7, 11, 15], 9))     # Saída: [0, 1]
print(twoSum([3, 2, 4], 6))          # Saída: [1, 2]
print(twoSum([3, 3], 6))             # Saída: [0, 1]
print(twoSum([1, 2, 3, 4, 5], 8))    # Saída: [2, 4]
print(twoSum([1, 2, 3, 4, 5], 10))   # Saída: []