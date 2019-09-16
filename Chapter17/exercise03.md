### Write a Python program that creates a new database and executes the following SQL statements. How do the results of the SELECT statements differ from what you would expect Python itself to do? Why?

```python
>>> value = 1
>>> 1/0
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 1/0 and value > 0
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> value > 0 and 1/0
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

> In SQL, division by zero results in a special value that represents infinity (if the
numerator is not zero) or “not a number” when the numerator is zero. However, even 
though this special value is non-zero it does not evaluate to True. So in each select
statement, no rows are returned.

