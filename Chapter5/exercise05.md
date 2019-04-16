### In ​Functions That Python Provides​, we saw built-in function abs. 
### Variable x refers to a number. 
### Write an expression that evaluates to True if x and its absolute value are equal and evaluates to False otherwise. 
### Assign the resulting value to a variable named result.

```python

x = 0
x = input("Enter value of X : ")
x = int(x)
trueValueX = x
absValueX = abs(x)

def CheckValue (x: int) -> bool:
    if trueValueX == absValueX:
        result = True
    else:
        result = False
    
    return result
    
print(CheckValue(x))

```

