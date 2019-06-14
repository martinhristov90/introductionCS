In this exercise, you will implement class Country, which represents a country with a name, a population, and an area.

1. Here is a sample interaction from the Python shell:
```python
>>> canada = Country('Canada', 34482779, Ó984670)
>>> canada.name
'Canada'
>>> canada.population
34482779
>>> canada.area
9984670
```
This code cannot be executed yet because class Country does not exist. Define Country with a constructor (method __init__) that has four parameters: a country, its name, its population, and its area.

2. Consider this code:
```python
>>> canada = Country('Canada', 34482779, 9984670)
>>> usa = Country('United States of America', 313914040, 9826675)
>>> canada.is_larger(usa)
True
```
In class Country, define a method named is_larger that takes two Country objects and returns True if and only if the first has a larger area than the second.

3. Consider this code:
```python
>>> canada.population_density()
3.4535722262227995
```
In class Country, define a method named population_density that returns the population density of the country (people per square kilometer).

4. Consider this code:
```python
>>> usa = Country('United States of America', 313914040, 9826675)
>>> print(usa)
United States of America has a population of 313914040 and is 9826675
square km.
```
In class Country, define a method named __str__ that returns a string representation of the country in the format shown here.

5. After you have written __str__, this session shows that a __repr__ method would be useful:
```python
>>> canada = Country('Canada', 34482779, 9984670)
>>> canada
<exercise_country.Country object at 0x7f2aba30b550>
>>> print(canada)
Canada has population 34482779 and is 9984670 square km.
>>> [canada]
[<exercise_country.Country object at 0x7f2aba30b550>]
>>> print([canada])
[<exercise_country.Country object at 0x7f2aba30b550>]
```
Define the __repr__ method in Country to produce a string that behaves like this:
```python
>>> canada = Country('Canada', 34482779, 9984670)
>>> canada
Country('Canada', 34482779, 9984670)
>>> [canada]
[Country('Canada', 34482779, 9984670)]
```

## Answers :

1. 
```python
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
```

2. 
```python
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other):
        if isinstance(other,Country):
            return self.area > other.area
        else:
            print("Both objects need to be from class Country")
            return -1
```

3. 
```python
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other):
        if isinstance(other,Country):
            return self.area > other.area
        else:
            print("Both objects need to be from class Country")
            return -1
    
    def population_density(self):
        return (self.population / self.area)
```

4. 
```python
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other):
        if isinstance(other,Country):
            return self.area > other.area
        else:
            print("Both objects need to be from class Country")
            return -1
    
    def population_density(self):
        return (self.population / self.area)

    def __str__(self):
        return ("{0} has a population of {1} and its area is {2} square kilometers.".format(self.name,self.population,self.area))
```

5. 
```python
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other):
        if isinstance(other,Country):
            return self.area > other.area
        else:
            print("Both objects need to be from class Country")
            return -1
    
    def population_density(self):
        return (self.population / self.area)

    def __str__(self):
        return ("{0} has a population of {1} and its area is {2} square kilometers.".format(self.name,self.population,self.area))
    
    def __repr__(self):
        # Using self.__class__.__name__ to get the object's class name, it returns 'str'
        return "{0}({1},{2},{3})".format(self.__class__.__name__,self.name,self.population,self.area)
```
