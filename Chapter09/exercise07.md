### Consider the following statement, which creates a list of populations of countries in eastern Asia (China, DPR Korea, Hong Kong, Mongolia, Republic of Korea, and Taiwan) in millions: country_populations = [1295, 23, 7, 3, 47, 21]. Write a for loop that adds up all the values and stores them in variable total. (Hint: Give total an initial value of zero, and, inside the loop body, add the population of the current country to total.)

```python

total = 0
country_populations = [1295, 23, 7, 3, 47, 21]

for i in range(len(country_populations)):
    total = total + country_populations[i]

print("Total population : {0} ".format(total))

>>> Total population : 1396 
```