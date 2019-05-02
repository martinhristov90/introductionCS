### Write a program that makes a backup of a file. 
### Your program should prompt the user for the name of the file to copy and then write a new file with the same contents but with .bak as the file extension.

```python

fileName = input('Please, enter the name of the file that you wish to make .bak file for ')
fileContent = ''

with open(fileName, 'r') as fd:
    fileContent = fd.read()

with open(fileName + '.bak', 'w') as fd:
    fd.write(fileContent)
    
```