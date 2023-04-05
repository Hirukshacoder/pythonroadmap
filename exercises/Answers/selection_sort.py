List = [3, 4, 5, 6]

def selection_sort(List):
    for i in range(0, len(List)-1):
        curr_minidx = i
        for j in range(i + 1, len(List)):
            if List[j] < List[curr_minidx]:
                curr_minidx = j
                
        List[i], List[curr_minidx] = List[curr_minidx], List[i]
    
selection_sort(List)
print(List)
