## In the description of bubble sort in the previous exercise, the sorted section of the list was at the end of the list. In this exercise, bubble sort will maintain the sorted section at the beginning of the list. Make sure that you are still implementing bubble sort!

- Rewrite the English description of bubble sort from the previous exercise with the necessary changes so that the sorted elements are at the beginning of the list instead of at the end.
    - Answer :
        - A variable called `index` is going to be used for indexing the elements.
        - Initial value is equal to 0.
        - While `index` is smaller than the length of the array (just smaller < , not <=)
        - Go and compare each element with its adjacent one, if the adjacent element is smaller, swap the two elements
        - Increase index with 1 in each iteration.

- Using your English description of bubble sort, write an outline of the bubble sort algorithm in English.
    - Answer :
        - A variable called `index` is going to be used for indexing the elements.
        - index = 0
        - index < len(array) 
        - while the above is true :
        - Go and compare each element with its adjacent(previous) one, if the adjacent(previous) element is smaller, swap the two elements.
        - index = index + 1

- Write function bubble_sort_2(L).
    - Answer :
        ```python
        def bubble_sort_2(array):
            index = 0
            while index < len(array):
                for j in range(len(array) - 1,index,-1):
                    if array[j] > array[j-1]:
                        array[j], array[j-1] = array[j-1], array[j]
                index += 1
            return array
        ```

- Try it out on the test cases from selection_sort.