### In this exercise, you’ll create a list and then answer questions about that list.


- Create a list of temperatures in degrees Celsius with the values 25.2, 16.8, 31.4, 23.9, 28, 22.5, and 19.6, and assign 
it to a variable called temps.
    ```python
    >>> temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
    >>> temps
    [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
    >>> 
    ```
- Using one of the list methods, sort temps in ascending order.
    ```python
    >>> temps.sort()
    >>> temps
    [16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
    >>> 
    ```
- Using slicing, create two new lists, cool_temps and warm_temps, which contain the temperatures below and above 20 degrees Celsius, respectively.
    ```python
    >>> cold_temps = temps[:2]
    >>> cold_temps
    [16.8, 19.6]
    >>> warm_temps = temps[3:]
    >>> warm_temps
    [23.9, 25.2, 28, 31.4]
    >>> 
    ```
- Using list arithmetic, recombine cool_temps and warm_temps into a new list called temps_in_celsius.
    ```python
    >>> temps_in_celsius = cold_temps + warm_temps
    >>> temps_in_celsius
    [16.8, 19.6, 23.9, 25.2, 28, 31.4]
    >>> 
    ```