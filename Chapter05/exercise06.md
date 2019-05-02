### Write a function named different that has two parameters, a and b. 
### The function should return True if a and b refer to different values and should return False otherwise.

```python

def CheckValues(a: int, b: int ) -> bool:
    result = None
    if a != b :
        result = True
    else :
        result = False
    return(result)

print(CheckValues(3,3))

print(CheckValues(2,3))

```