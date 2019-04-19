### Variable appointments refers to the list ['9:00', '10:30', '14:00', '15:00', '15:30']. 
### An appointment is scheduled for 16:30, so '16:30' needs to be added to the list.

- Using list method append, add ’16:30’ to the end of the list that appointments refers to.
    ```python
    >>> times = ['9:00', '10:30', '14:00', '15:00', '15:30']
    >>> times.append('16:30')
    >>> times
    ['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
    >>> 
    ```
- Instead of using append, use the + operator to add ’16:30’ to the end of the list that appointments refers to.

    ```python
    >>> times = ['9:00', '10:30', '14:00', '15:00', '15:30']
    >>> times + ['16:30']
    ['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
    >>> 
    ```
- You used two approaches to add ’16:30’ to the list. Which approach modified the list and which approach created a new list? 
    > The second one.