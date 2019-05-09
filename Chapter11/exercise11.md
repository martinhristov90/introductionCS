### Write another function called db_consistent that takes a dictionary of dictionaries in the format described in the previous question and returns True if and only if every one of the inner dictionaries has exactly the same keys. (This function would return False for the previous example, since Rosalind Franklin’s entry doesn’t contain the ’author’ key.)

### Previous example :

```python

{
  'jgoodall'  : {'surname'  : 'Goodall',
                 'forename' : 'Jane',
                 'born'     : 1934,
                 'died'     : None,
                 'notes'    : 'primate researcher',
                 'author'   : ['In the Shadow of Man',
                               'The Chimpanzees of Gombe']},
  'rfranklin' : {'surname'  : 'Franklin',
                 'forename' : 'Rosalind',
                 'born'     : 1920,
                 'died'     : 1957,
                 'notes'    : 'contributed to discovery of DNA'},


   'rcarson'  : {'surname'  : 'Carson',
                 'forename' : 'Rachel',
                 'born'     : 1907,
                 'died'     : 1964,
                 'notes'    : 'raised awareness of effects of DDT',
                 'author'   : ['Silent Spring']}
}

```

### Answer : 

```python
def db_consistent(inDict):
    innerDictKeys = []

    for outerKey in inDict:
        tempKeys = list(inDict[outerKey].keys())
        tempKeys.sort()
        innerDictKeys.append(tempKeys)

    for i in range(1,len(innerDictKeys)):
        if len(innerDictKeys[0]) != len(innerDictKeys[i]):
            return False

        for j in range(len(innerDictKeys[0])):
            if innerDictKeys[0][j] != innerDictKeys[i][j]:
                return False

    return True



testDict = {
    'jgoodall'  : {'surname'  : 'Goodall',
                    'forename' : 'Jane',
                    'born'     : 1934,
                    'died'     : None,
                    'notes'    : 'primate researcher',
                    'author'   : ['In the Shadow of Man',
                                'The Chimpanzees of Gombe']},
    'rfranklin' : {'surname'  : 'Franklin',
                    'forename' : 'Rosalind',
                    'born'     : 1920,
                    'died'     : 1957,
                    'notes'    : 'contributed to discovery of DNA'},


    'rcarson'  : {'surname'  : 'Carson',
                    'forename' : 'Rachel',
                    'born'     : 1907,
                    'died'     : 1964,
                    'notes'    : 'raised awareness of effects of DDT',
                    'author'   : ['Silent Spring']}
    }

# How to use it :

print(db_consistent(testDict))

```