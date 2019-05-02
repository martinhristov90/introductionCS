### 1. Import module math, and use its functions to complete the following exercises. (You can call dir(math) to get a listing of the items in math.)

- Write an expression that produces the floor of -2.8.
- Write an expression that rounds the value of -4.3 and then produces the absolute value of that result.
- Write an expression that produces the ceiling of the sine of 34.5.

### 2. In the following exercises, you will work with Python’s calendar module:

- Visit the Python documentation website at http://docs.python.org/release/3.6.0/py-modindex.html, and look at the documentation on module calendar.
- Import module calendar.
- Using function help, read the description of function isleap.
- Use isleap to determine the next leap year.
- Use dir to get a list of what calendar contains.
- Find and use a function in module calendar to determine how many leap years there will be between the years 2000 and 2050, inclusive.
- Find and use a function in module calendar to determine which day of the week July 29, 2016, will be.

### 3. Create a file named exercise.py with this code inside it:

```python
​ 	​def​ average(num1: float, num2: float) -> float:
​ 	    ​"""Return the average of num1 and num2.​
​ 	
​ 	​    >>> average(10,20)​
​ 	​    15.0​
​ 	​    >>> average(2.5, 3.0)​
​ 	​    2.75​
​ 	​    """​
​ 	
​ 	    ​return​ num1 + num2 / 2
``` 
- Run exercise.py. Import doctest and run doctest.testmod().

- Both of the tests in function average’s docstring fail. Fix the code and rerun the tests. Repeat this procedure until the tests pass.