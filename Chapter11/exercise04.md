### The PDB file format is often used to store information about molecules. A PDB file may contain zero or more lines that begin with the word AUTHOR (which may be in uppercase, lowercase, or mixed case), followed by spaces or tabs, followed by the name of the person who created the file. Write a function that takes a list of filenames as an input argument and returns the set of all author names found in those files.

```python

from typing import List

def authors(files: List) -> str:
    """
    Return list of Authors' names.
    """
    authors = []

    for fd in files:
        with open(fd) as file:
            for line in file:
                if line.lower().startswith('author') :
                    newline = line.lower().strip('author').strip()
                    authors.append(newline.capitalize())
    
    return authors

#How to use it : 
print(authors(['test.txt']))

```