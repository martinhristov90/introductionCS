### Exercises

Here are some exercises for you to try on your own. Solutions are available at http://pragprog.com/titles/gwpy3/practical-programming.

### 1. What value does each of the following expressions evaluate to? Verify your answers by typing the expressions into the Python shell.

- ’Computer’ + ’ Science’
- ’Darwin\’s’
- ’H2O’ * 3
- ’CO2’ * 0

### 2. Express each of the following phrases as Python strings using the appropriate type of quotation marks (single, double, or triple) and, if necessary, escape sequences. There is more than one correct answer for each of these phrases.

- They’ll hibernate during the winter.
- “Absolutely not,” he said.
- “He said, ‘Absolutely not,’” recalled Mel.
- hydrogen sulfide
- left\right

### 3. Rewrite the following string using single or double quotes instead of triple quotes:

```python 
​ 	​'''A​
​ 	​B​
​ 	​C'''​
```

### 4. Use built-in function len to find the length of the empty string.

### 5. Given variables x and y, which refer to values 3 and 12.5, respectively, use function print to print the following messages. When numbers appear in the messages, variables x and y should be used.

- The rabbit is 3.
- The rabbit is 3 years old.
- 12.5 is average.
- 12.5 * 3
- 12.5 * 3 is 37.5.

### 6. Consider this code:

```python
​ 	​>>>​​ ​​first​​ ​​=​​ ​​'John'​
​ 	​>>>​​ ​​last​​ ​​=​​ ​​'Doe'​
​ 	​>>>​​ ​​print(last​​ ​​+​​ ​​', '​​ ​​+​​ ​​first)​
What is printed by this code?
```

### 7. Use input to prompt the user for a number, store the number entered as a float in a variable named num, and then print the contents of num.

### 8. Complete the examples in the docstring and then write the body of the following function:
```python
​ 	​def​ repeat(s: str, n: int) -> str:
​ 	    ​""" Return s repeated n times; if n is negative, return the empty string.​
​ 	
​ 	​    >>> repeat('yes', 4)​
​ 	​    'yesyesyesyes'​
​ 	​    >>> repeat('no', 0)​
​ 	
​ 	​    >>> repeat('no', -2)​
​ 	
​ 	​    >>> repeat('yesnomaybe', 3)​
​ 	
​ 	​    """​
```
### 9. Complete the examples in the docstring and then write the body of the following function:
```python
​ 	​def​ total_length(s1: str, s2: str) -> int:
​ 	    ​""" Return the sum of the lengths of s1 and s2.​
​ 	
​ 	​    >>> total_length('yes', 'no')​
​ 	​    5​
​ 	​    >>> total_length('yes', '')​
​ 	
​ 	​    >>> total_length('YES!!!!', 'Noooooo')​
​ 	
​ 	​    """​
```