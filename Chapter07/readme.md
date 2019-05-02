### 1. In the Python shell, execute the following method calls:

- ’hello’.upper()
- ’Happy Birthday!’.lower()
- ’WeeeEEEEeeeEEEEeee’.swapcase()
- ’ABC123’.isupper()
- ’aeiouAEIOU’.count(’a’)
- ’hello’.endswith(’o’)
- ’hello’.startswith(’H’)
- ’Hello {0}’.format(’Python’)
- ’Hello {0}! Hello {1}!’.format(’Python’, ’World’)

### 2. Using string method count, write an expression that produces the number of o’s in ’tomato’.

### 3. Using string method find, write an expression that produces the index of the first occurrence of o in ’tomato’.

### 4. Using string method find, write a single expression that produces the index of the second occurrence of o in ’tomato’. Hint: Call find twice.

### 5. Using your expression from the previous exercise, find the second o in ’avocado’. If you don’t get the result you expect, revise the expression and try again.

### 6. Using string method replace, write an expression that produces a string based on ’runner’ with the n’s replaced by b’s.

### 7. Variable s refers to ’  yes    ’. When a string method is called with s as its argument, the string ’yes’ is produced. Which string method was called?

### 8. Variable fruit refers to ’pineapple’. For the following function calls, in what order are the subexpressions evaluated?

- fruit.find(’p’, fruit.count(’p’))
- fruit.count(fruit.upper().swapcase())
- fruit.replace(fruit.swapcase(), fruit.lower())

### 9. Variable season refers to ’summer’. Using string method format and variable season, write an expression that produces ’I love summer!’

### 10. Variables side1, side2, and side3 refer to 3, 4, and 5, respectively. Using string method format and those three variables, write an expression that produces ’The sides have lengths 3, 4, and 5.’

### 11. Using string methods, write expressions that produce the following:

- A copy of ’boolean’ capitalized
- The first occurrence of ’2’ in ’CO2 H2O’
- The second occurrence of ’2’ in ’CO2 H2O’
- True if and only if ’Boolean’ begins lowercase
- A copy of "MoNDaY" converted to lowercase and then capitalized
- A copy of "   Monday" with the leading whitespace removed

### 12. Complete the examples in the docstring and then write the body of the following function:
```python
​ 	​def​ total_occurrences(s1: str, s2: str, ch: str) -> int:
​ 	    ​"""Precondition: len(ch) == 1​
​ 	
​ 	​    Return the total number of times that ch occurs in s1 and s2.​
​ 	
​ 	​    >>> total_occurrences('color', 'yellow', 'l')​
​ 	​    3​
​ 	​    >>> total_occurrences('red', 'blue', 'l')​
​ 	
​ 	​    >>> total_occurrences('green', 'purple', 'b')​
​ 	
​ 	​    """​
```