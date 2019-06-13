In this exercise, you will implement a Continent class, which represents a continent with a name and a list of countries. Class Continent will use class Country from the previous exercise. If Country is defined in another module, you’ll need to import it.

1. Here is a sample interaction from the Python shell:
```python
>>> canada = country.Country('Canada', 34482779, 9984670)
>>> usa = country.Country('United States of America', 313914040,
...                       9826675)
>>> mexico = country.Country('Mexico', 112336538, 1943950)
>>> countries = [canada, usa, mexico]
>>> north_america = Continent('North America', countries)
>>> north_america.name
'North America'
>>> for country in north_america.countries:
    print(country)
```
Canada has a population of 34482779 and is 9984670 square km.
United States of America has a population of 313914040 and is 9826675
square km.
Mexico has a population of 112336538 and is 1943950 square km.
>>>
The code cannot be executed yet, because class Continent does not exist. Define Continent with a constructor (method __init__) that has three parameters: a continent, its name, and its list of Country objects.

2. Consider this code:
```python
>>> north_america.total_population()
460733357
```
In class Continent, define a method named total_population that returns the sum of the populations of the countries on this continent.

3. Consider this code:
```python
>>> print(north_america)
North America
Canada has a population of 34482779 and is 9984670 square km.
United States of America has a population of 313914040 and is 9826675
square km.
Mexico has a population of 112336538 and is 1943950 square km.
```
In class Continent, define a method named __str__ that returns a string representation of the continent in the format shown here.

## Answers:

1. 
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
        return "{0}({1},{2},{3})".format(self.__class__.__name__,self.name,self.population,self.area)

class Continent(Country):
    def __init__(self,continentName,countryList):
        self.continentName = continentName
        self.countryList = countryList[:]

canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040,9826675)
mexico = Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)

for country in north_america.countryList:
    print(country)
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
    
    def population_density(self):
        return (self.population / self.area)

    def __str__(self):
        return ("{0} has a population of {1} and its area is {2} square kilometers.".format(self.name,self.population,self.area))
    
    def __repr__(self):
        return "{0}({1},{2},{3})".format(self.__class__.__name__,self.name,self.population,self.area)

class Continent(Country):
    def __init__(self,continentName,countryList):
        self.continentName = continentName
        self.countryList = countryList[:]
    
    def total_population(self):
        populationSum = 0
        for i in range(len(self.countryList)):
            populationSum = populationSum + self.countryList[i].population
        return populationSum

canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040,9826675)
mexico = Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)

print(north_america.total_population())
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

    def __str__(self):
        return ("{0} has a population of {1} and its area is {2} square kilometers.".format(self.name,self.population,self.area))
    
    def __repr__(self):
        return "{0}({1},{2},{3})".format(self.__class__.__name__,self.name,self.population,self.area)

class Continent(Country):
    def __init__(self,continentName,countryList):
        self.continentName = continentName
        self.countryList = countryList[:]
    
    def total_population(self):
        populationSum = 0
        for i in range(len(self.countryList)):
            populationSum = populationSum + self.countryList[i].population
        return populationSum

    def __str__(self):
        output = self.continentName + "\n"
        for i in self.countryList:
            output = output + i.__str__() + "\n"
        return output


canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040,9826675)
mexico = Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)

print(north_america)

```
