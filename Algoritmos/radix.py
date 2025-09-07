
def manual_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def manual_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val



def manual_append(lst, item):
    new_lst = [None] * (manual_len(lst) + 1)
    for i in range(manual_len(lst)):
        new_lst[i] = lst[i]
    new_lst[manual_len(lst)] = item
    return new_lst

def manual_extend(lst1, lst2):
    new_lst = [None] * (manual_len(lst1) + manual_len(lst2))
    for i in range(manual_len(lst1)):
        new_lst[i] = lst1[i]
    for i in range(manual_len(lst2)):
        new_lst[manual_len(lst1) + i] = lst2[i]
    return new_lst

def radix_sort(list:list[int]):
    if not list:
        return list

    max_val = manual_max(list)

    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        
        for num in list:
            digit = (num // exp) % 10
            buckets[digit] = manual_append(buckets[digit], num)
        
        list = []
        for bucket in buckets:
            list = manual_extend(list, bucket)
        
        exp *= 10
    
    return list

# # Exemplo de uso
# if __name__ == "__main__":
#     arr = [170, 45, 75, 90, 802, 24, 2, 66]
#     print("Array original:", arr)
#     arr = radix_sort(arr)
#     print("Array ordenado:", arr)