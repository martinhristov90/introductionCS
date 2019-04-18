### Using string methods, write expressions that produce the following:

- A copy of ’boolean’ capitalized.
    ```python
    >>> 'boolean'.capitalize()
    'Boolean'
    ```
- The first occurrence of ’2’ in ’CO2 H2O’.
    ```python
    'CO2 H2O'.find('2')
    >>> 'CO2 H2O'.find('2')
    2
    >>> 
    ```
- The second occurrence of ’2’ in ’CO2 H2O’.
    ```python
    'CO2 H2O'.find('2','CO2 H2O'.find('2') + 1)
    ```
- True if and only if ’Boolean’ begins lowercase.
    ```python
    >>> 'Boolean'[0].islower()
    False
    ```
- A copy of "MoNDaY" converted to lowercase and then capitalized.
    ```python
    >>> 'MoNDaY'.lower().capitalize()
    'Monday'
    >>> 
    ```
- A copy of "   Monday" with the leading whitespace removed.
    ```python
        >>> '   Monday'.lstrip()
        'Monday'
        >>> 
    ```
