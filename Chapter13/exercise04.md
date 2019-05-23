### Given the unsorted list [6, 5, 4, 3, 7, 1, 2], show what the contents of the list would be after each iteration of the loop as it is sorted using the following:

- Selection sort

- Answer: 

    ```python

    def find_min (lst: list, element: int) -> int:
        smallest = element
        i = element + 1

        while i != len(lst):
        
            if lst[i] < lst[smallest]:
                smallest = i

            i = i + 1

        return smallest

    def selection_sort(L: list) -> list:

        i = 0

        while i != len(L):
            smallest = find_min(L,i)
            # Swaps the values
            L[i], L[smallest] = L[smallest], L[i]
            i = i + 1

        return L

    ```

    ```
    - List unsorted     : [6, 5, 4, 3, 7, 1, 2]

    - First iteration   : [1, 5, 4, 3, 7, 6, 2]
    - Second iteration  : [1, 2, 4, 3, 7, 6, 5]
    - Third iteration   : [1, 2, 3, 4, 7, 6, 5]
    - Forth iteration   : [1, 2, 3, 4, 7, 6, 5]
    - Fifth iteration   : [1, 2, 3, 4, 5, 6, 7]
    - Sixth iteration   : [1, 2, 3, 4, 5, 6, 7]
    ```

- Insertion sort
    ```python
    def insert(L: list, element: int) -> None:

        i = element

        # Decreasing i until we find element larger that the one passed to the function. Backwards !
        # i != 0 statement is there in case every value in the list is greater than the element.

        while i != 0 and L[i-1] >= L[element]:
            i = i - 1

        value = L[element]
        del L[element]
        L.insert(i,value)

        return L


    def insertion_sort(L: list) -> None:
        i = 0

        while i != len(L):
            insert(L,i)
            i += 1
    ```
    ```
    - List unsorted     : [6, 5, 4, 3, 7, 1, 2]

    - First iteration   : [6, 5, 4, 3, 7, 1, 2]
    - Second iteration  : [5, 6, 4, 3, 7, 1, 2]
    - Third iteration   : [4, 5, 6, 3, 7, 1, 2]
    - Forth iteration   : [3, 4, 5, 6, 7, 1, 2]
    - Fifth iteration   : [3, 4, 5, 6, 7, 1, 2]
    - Sixth iteration   : [1, 3, 4, 5, 6, 7, 2]
    - Seventh iteration : [1, 2, 3, 4, 5, 6, 7]
    - Eight iteration   : [1, 2, 3, 4, 5, 6, 7]
    ```


