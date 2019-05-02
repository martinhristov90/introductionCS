### Redo the previous two exercises using while loops instead of for loops.

- 1. The solution to exercise 13 :

> ```python
> 
> for i in range(1,8):
> 
>     for j in range(i):
> 
>         print("T",end="")
>         
>     print("\r")
> 
> ```

- Redone with while loops instead for loops :

```python

i = 1
j = 0

while i <= 8:
    i = i + 1

    while j <= i:
        j = j + 1
        print("T",end="")
        
    j = 0
    print("\r")


```

- 2. The solution to exercise 14 :

> ```python
> 
> for i in range(1,8):
> 
>     print(" " * (7 - i),end="")
> 
>     for j in range(i):
> 
>         print("T",end="")
>         
>     print("\r")
>         
> ```

- Redone with while loops instead for loops :

```python
i = 0
j = 0

while i <= 8:
    

    print(" " * (8 - i),end="")

    while j <= i:

        j = j + 1
        
        print("T",end="")
        
    print("\r")
    i = i + 1
    j = 0
```