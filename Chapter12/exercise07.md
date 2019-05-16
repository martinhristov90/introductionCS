### This one is a fun challenge.

### Edsgar Dijkstra is known for his work on programming languages. He came up with a neat problem that he called the Dutch National Flag problem: given a list of strings, each of which is either ’red’, ’green’, or ’blue’ (each is repeated several times in the list), rearrange the list so that the strings are in the order of the Dutch national flag—all the ’red’ strings first, then all the ’green’ strings, then all the ’blue’ strings.

- Write a function called dutch_flag that takes a list and solves this problem.

```python

def dutch_flag(inList):
    finalLst = []

    for i in inList:
        if i == "red":
            finalLst.append(i)
    for i in inList:
        if i == "green":
            finalLst.append(i)
    for i in inList:
        if i == "blue":
            finalLst.append(i)

    return finalLst

print(dutch_flag(['red', 'green', 'blue', 'red', 'red', 'blue', 'red','green']))

```