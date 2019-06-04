## Modify the timing program to compare bubble sort with insertion and selection sort. Explain the results.

```python
import time
import selection_sort
import insertion_sort
import bubble_sort

from typing import Callable, Any

def time_it(sortAlg: Callable[[list,Any],Any], L: list) -> float:

    t1 = time.perf_counter()
    sortAlg(L)
    t2 = time.perf_counter()
    return (t2-t1) * 1000.0

def print_times(L: list) -> None:
    
    # Now testing my functions

    selection_time = time_it(selection_sort.selection_sort,L)
    insertion_time = time_it(insertion_sort.insertion_sort,L)
    bubble_time = time_it(bubble_sort.bubble_sort,L)


    #if v == 10000000:
    print("{0}\t{1:.2f}\t\t{2:.2f}\t".format(selection_time, insertion_time, bubble_time))
    #else:
    #   print("{0}\t\t{1:.2f}\t\t{2:.2f}\t".format(while_time, sentinel_time, index_time))


L = list(reversed(range(20)))
L1 = list(reversed(range(200)))
L2 = list(reversed(range(2000)))
print("selection_time\tinsertion_time\tbubble_time")

print_times(L)
print_times(L1)
print_times(L2)

```

- Results : 

|Size|selection_time|insertion_time|bubble_time|
|:-:|:-:|---|---|
|20|0.05979899|0.02|0.04|
|200|4.9842900|0.22|2.52|
|2000|346.306324|2.50|192.06|

NB : In order to execute the code above, you need the modules located in directory "Assets_Needed_exercise7" to be in the same folder.
