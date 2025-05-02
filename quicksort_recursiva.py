def quicksort(arr, left, right):
    if left < right:
        print(arr[left:right+1])
        pi = partition(arr, left, right) # posicao da partição
        quicksort(arr, left, pi - 1)
        quicksort(arr, pi + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] #anda no j até enmcontrar o menor
    # Troca o pivô com o elemento na posição i + 1
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr)-1)