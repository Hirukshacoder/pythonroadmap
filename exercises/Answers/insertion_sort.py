List = [1, 5, 4, 6]
def insertion_sort(List):
    for i in range(1, len(List)):
        j = i
        while List[j-1] > List[j] and List[j] > 0:
            List[j-1], List[j] = List[j], List[j-1]
            j -= 1
insertion_sort(List)
print(List)
