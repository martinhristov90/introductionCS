### Repeat the previous exercise using negative indices.

- The first item of units (the first inner list)
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][-2]
    ['km', 'miles', 'league']
    >>> 
    ```
- The last item of units (the last inner list)
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][-1]
    [['kg', 'pound', 'stone']]
    >>> 
    ```
- The string 'km'
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][-2][-3]
    'km'
    >>> 
    ```
- The string 'kg'
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][-1][-3]
    'kg'
    >>> 
    ```
- The list ['miles', 'league']
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][-2][-2:]
    ['miles', 'league']
    >>> 
    ```
- The list ['kg', 'pound']  
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][-1][-3:-1]
    ['kg', 'pound']
    >>> 
    ```