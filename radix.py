def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        
        exp *= 10
    
    return arr

# Exemplo de uso
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Array original:", arr)
    arr = radix_sort(arr)
    print("Array ordenado:", arr)