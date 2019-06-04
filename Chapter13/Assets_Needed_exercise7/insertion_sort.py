
def insert(L: list, element: int) -> None:
    
    i = element

    # Decreasing i until we find element larger that the one passed to the function. Backwards !
    # i != 0 statment is there in case every value in the list is greater than the element.
    while i != 0 and L[i-1] >= L[element]:
        i = i - 1
        
    value = L[element]
    del L[element]
    L.insert(i,value)


def insertion_sort(L: list) -> list:
    i = 0
    while i != len(L):
        insert(L,i)
        i += 1
    return L

