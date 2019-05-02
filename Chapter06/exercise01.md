### Import module math, and use its functions to complete the following exercises. 
### (You can call dir(math) to get a listing of the items in math.)

    1. Write an expression that produces the floor of -2.8.
    2. Write an expression that rounds the value of -4.3 and then produces the absolute value of that result.
    3. Write an expression that produces the ceiling of the sine of 34.5.

- 1. According to [w3schools](https://www.w3schools.com/jsref/jsref_floor.asp) the "floor" function "Round a number downward to its nearest integer".
    ```python
        >>> math.floor(-2.8)
    -3
    ```

- 2. We need to use round() to round the value, and abs() to produce the absolute value.
    ```python
    abs(round(-4.3))
    ```
    
- 3. We need to use math.sin() to calculate the sine of 34.5, it needs to be called math.sin() not jut sin(), and math.ceil(). According to [w3schools](https://www.w3schools.com/jsref/jsref_ceil.asp) the "ceil" function "Round a number upward to its nearest integer".
    ```python
    math.ceil(math.sin(34.5))
    ```