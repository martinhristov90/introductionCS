### Sorted section at the end of the list. The list is traversed, pairs of elements are compared, and larger elements are swapped into the higher position. This is repeated until all elements are sorted.

1. Using the English description of bubble sort, write an outline of the bubble sort algorithm in English.
    - Answer :
        - A variable called `index` is going to be used for indexing the elements.
        - Initial value is equal to length of the array minus 1.
        - While `index` is greater or equal to 0.
        - Go and compare each element with its adjacent one, if the adjacent element is larger, swap the two elements
        - Reduce index with 1

2. Continue using top-down design until you have a Python algorithm.
    - Answer :
        - index = len(array) - 1
        - while index >= 0
        - Go and compare each element with its adjacent one, if the adjacent element is larger, swap the two elements.
        - index = index - 1 

3. Turn it into a function called bubble_sort(L).
    - Answer :
    ```python
    def bubble_sort(array):
        index = len(array) - 1
        while index >= 0:
            for j in range(index):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
            index -= 1
        return array
    ```

4. Try it out on the test cases from selection_sort.
    