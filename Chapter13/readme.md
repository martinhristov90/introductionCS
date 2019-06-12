## 1. Rewrite the English description of bubble sort from the previous exercise with the necessary changes so that the sorted elements are at the beginning of the list instead of at the end.

## 2. Using your English description of bubble sort, write an outline of the bubble sort algorithm in English.

## 3. Write function bubble_sort_2(L).

## 4. Try it out on the test cases from selection_sort.

## 5. Modify the timing program to compare bubble sort with insertion and selection sort. Explain the results.

## 6. The analysis of bin_sort said, “Since N values have to be inserted, the overall running time is N log2 N.” Point out a flaw in this reasoning, and explain whether it affects the overall conclusion.

## 7. There are at least two ways to come up with loop conditions. One of them is to answer the question, “When is the work done?” and then negate it. In function merge in ​Merging Two Sorted Lists​, the answer is, “When we run out of items in one of the two lists,” which is described by this expression: i1 == len(L1) or i2 == len(L2). Negating this leads to our condition i1 != len(L1) and i2 != len(L2).

## 8. Another way to come up with a loop condition is to ask, “What are the valid values of the loop index?” In function merge, the answer to this is 0 <= i1 < len(L1) and 0 <= i2 < len(L2); since i1 and i2 start at zero, we can drop the comparisons with zero, giving us i1 < len(L1) and i2 < len(L2).

## 9. Is there another way to do it? Have you tried both approaches? Which do you prefer?

## 10. In function mergesort in ​Merge Sort​, there are two calls to extend. They are there because when the preceding loop ends, one of the two lists still has items in it that haven’t been processed. Rewrite that loop so that these extend calls aren’t needed.