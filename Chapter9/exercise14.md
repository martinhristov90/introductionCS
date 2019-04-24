### Using nested for loops, print the triangle described in the previous exercise with its hypotenuse on the left side:

```python

for i in range(1,8):

    print(" " * (7 - i),end="")

    for j in range(i):

        print("T",end="")
        
    print("\r")
        
```