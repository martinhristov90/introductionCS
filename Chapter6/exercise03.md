### Create a file named exercise.py with this code inside it:

```python
 ​def​ average(num1: float, num2: float) -> float:
​   """Return the average of num1 and num2.​
​   
​   >>> average(10,20)​
​   15.0​
​   >>> average(2.5, 3.0)​
​   2.75​
​   """​
​   
​   return​ num1 + num2 / 2
```
 - Run exercise.py. Import doctest and run doctest.testmod().
    ```python
        def avarage(num1: float, num2:float) -> float:
            """
            Return the average of num1 and num2.​
            >>> average(10,20)​
            15.0
            >>> average(2.5, 3.0)
            2.75​
            """
            return (num1 + num2) / 2 

    >>> doctest.testmod()
    **********************************************************************
    File "__main__", line 3, in __main__.avarage
    Failed example:
        average(10,20)​
    Exception raised:
        Traceback (most recent call last):
          File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/doctest.py", line 1329, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.avarage[0]>", line 1
            average(10,20)​
                          ^
        SyntaxError: invalid character in identifier
    **********************************************************************
    File "__main__", line 5, in __main__.avarage
    Failed example:
        average(2.5, 3.0)
    Exception raised:
        Traceback (most recent call last):
          File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/doctest.py", line 1329, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.avarage[1]>", line 1, in <module>
            average(2.5, 3.0)
        NameError: name 'average' is not defined
    **********************************************************************
    1 items had failures:
       2 of   2 in __main__.avarage
    ***Test Failed*** 2 failures.
    TestResults(failed=2, attempted=2)
    >>> 
    ```

 - Both of the tests in function average’s docstring fail. Fix the code and rerun the tests. Repeat this procedure until the tests pass.
    
    - The function "avarage" is misspelled in the docstring. There are whitespaces (Zero Width Space Unicode num : U+200B ) after the closing bracket on line 3 in the docstring and after number 5 on line 6.
     

    ```python
        def avarage(num1: float, num2:float) -> float:
            """
            Return the average of num1 and num2.​
            >>> avarage(10,20)
            15.0
            >>> avarage(2.5, 3.0)
            2.75
            """
            return (num1 + num2) / 2 
    ```