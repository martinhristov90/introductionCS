### Variables population and land_area refer to floats.
 
### Write an if statement that will print the population if it is less than 10,000,000.
 
### Write an if statement that will print the population if it is between 10,000,000 and 35,000,000.
 
### Write an if statement that will print “Densely populated” if the land density (number of people per unit of area) is ### greater than 100.
 
### Write an if statement that will print “Densely populated” if the land density (number of people per unit of area) is ### greater than 100, and “Sparsely populated” otherwise.

- Write an if statement that will print the population if it is less than 10,000,000.
   
    ```python 

    if population < 10000000:
        print(population)

    ```

- Write an if statement that will print the population if it is between 10,000,000 and 35,000,000.

    ```python

    if population > 10000000 and population < 35000000:
        print(population) 
    ```

- Write an if statement that will print “Densely populated” if the land density (number of people per unit of area) is ### greater than 100.

    ```python

    # We should divide the population over land_area, this would give us number of people per unit (km/miles)

    if (population / land_area) > 100:
        print('densely populated with over 100 people per unit ') 

    ```
- Write an if statement that will print “Densely populated” if the land density (number of people per unit of area) is greater than 100, and “Sparsely populated” otherwise.

    ```python

    if (population / land_area) > 100:
        print('densely populated with over 100 people per unit ') 
    else:
        print('Sparsely populated')

    ```