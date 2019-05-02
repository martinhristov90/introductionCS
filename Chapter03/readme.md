### 1.Two of Python’s built-in functions are min and max. In the Python shell, execute the following function calls:

min(2, 3, 4)

max(2, -3, 4, 7, -5)

max(2, -3, min(4, 7), -5)

### 2.For the following function calls, in what order are the subexpressions evaluated?

min(max(3, 4), abs(-5))

abs(min(4, 6, max(2, 8)))

round(max(5.572, 3.258), abs(-2))

### 3.Following the function design recipe, define a function that has one parameter, a number, and returns that number tripled.

### 4.Following the function design recipe, define a function that has two parameters, both of which are numbers, and returns the absolute value of the difference of the two. Hint: Call built-in function abs.

### 5.Following the function design recipe, define a function that has one parameter, a distance in kilometers, and returns the distance in miles. (There are 1.6 kilometers per mile.)

### 6.Following the function design recipe, define a function that has three parameters, grades between 0 and 100 inclusive, and returns the average of those grades.

### 7.Following the function design recipe, define a function that has four parameters, all of them grades between 0 and 100 inclusive, and returns the average of the best 3 of those grades. Hint: Call the function that you defined in the previous exercise.

### 8.Complete the examples in the docstring and then write the body of the following function:
```python
​ 	​def​ weeks_elapsed(day1, day2):
​ 	    ​""" (int, int) -> int​
​ 	
​ 	​    day1 and day2 are days in the same year. Return the number of full weeks​
​ 	​    that have elapsed between the two days.​
​ 	
​ 	​    >>> weeks_elapsed(3, 20)​
​ 	​    2​
​ 	​    >>> weeks_elapsed(20, 3)​
​ 	​    2​
​ 	​    >>> weeks_elapsed(8, 5)​
​ 	
​ 	​    >>> weeks_elapsed(40, 61)​
​ 	
​ 	​    """​
```
### 9. Consider this code:
```python
​ 	​def​ square(num):
​ 	    ​""" (number) -> number​
​ 	
​ 	​    Return the square of num.​
​ 	
​ 	​    >>> square(3)​
​ 	​    9​
​ 	​    """​
```
In the following table, fill in the Example column by writing square, num, square(3), and 3 next to the appropriate description.

Description
Example
Parameter
Argument
Function name
Function call

### 10. Write the body of the square function from the previous exercise.
