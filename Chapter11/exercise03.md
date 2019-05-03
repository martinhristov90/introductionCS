### Python’s set objects have a method called pop that removes and returns an arbitrary element from the set. If the set gerbils contains five cuddly little animals, for example, calling gerbils.pop() five times will return those animals one by one, leaving the set empty at the end. Use this to write a function called mating_pairs that takes two equal-sized sets called males and females as input and returns a set of pairs; each pair must be a tuple containing one male and one female. (The elements of males and females may be strings containing gerbil names or gerbil ID numbers—your function must work with both.)

```python 

from typing import Set

def mating_pairs(male: Set[str],female: Set[str]) -> Set[str]:

    if len(male) != len(female):
        print("The lenght of male and female sets should be equal")
    
    couples = set()

        couples = set()

    for i in range(len(male)):
        couples.add((male.pop(),female.pop()))
        
    return(couples)

print(mating_pairs({'marti','hristian'},{'kremi','stefka'}))

```