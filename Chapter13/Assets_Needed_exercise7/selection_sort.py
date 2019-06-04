def find_min (lst: list, element: int) -> int:
    smallest = element
    i = element + 1

    while i != len(lst):
        #print("I is  : {}".format(i))
        #print("Smallest is  : {}".format(smallest))
        if lst[i] < lst[smallest]:
            smallest = i
        i = i + 1

    return smallest

def selection_sort(L: list) -> list:

    i = 0
    
    while i != len(L):
        #print(L)
        smallest = find_min(L,i)
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1
    return L

