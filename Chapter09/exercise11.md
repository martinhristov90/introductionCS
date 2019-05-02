### Using a loop, sum the numbers in the range 2 to 22 (inclusive), and then calculate the average.

```python

total = 0
avarage = 0

for i in range(2,23):
    total = total + i

avarage = total / (len(range(2,23)))

print(avarage)

```