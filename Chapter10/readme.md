### 1. Write a program that makes a backup of a file. Your program should prompt the user for the name of the file to copy and then write a new file with the same contents but with .bak as the file extension.

### 2. Suppose the file alkaline_metals.txt contains the name, atomic number, and atomic weight of the alkaline earth metals:

​ 	beryllium 4 9.012
​ 	magnesium 12 24.305
​ 	calcium 20 20.078
​ 	strontium 38 87.62
​ 	barium 56 137.327
​ 	radium 88 226
- Write a for loop to read the contents of alkaline_metals.txt and store it in a list of lists, with each inner list containing the name, atomic number, and atomic weight for an element. (Hint: Use string.split.)

### 3. All of the file-reading functions we have seen in this chapter read forward through the file from the first character or line to the last. How could you write a function that would read backward through a file?

### 4. In ​Processing Whitespace-Delimited Data​, we used the “For Line in File” technique to process data line by line, breaking it into pieces using string method split. Rewrite function process_file to skip the header as normal but then use the Read technique to read all the data at once.

### 5. Modify the file reader in read_smallest_skip.py of ​Skipping the Header​ so that it can handle files with no data after the header.

### 6. Modify the file reader in read_smallest_skip.py of ​Skipping the Header​, so that it uses a continue inside the loop instead of an if. Which form do you find easier to read?

### 7. Modify the PDB file reader of ​Multiline Records​, so that it ignores blank lines and comment lines in PDB files. A blank line is one that contains only space and tab characters (that is, one that looks empty when viewed). A comment is any line beginning with the keyword CMNT.

### 8. Modify the PDB file reader to check that the serial numbers on atoms start at 1 and increase by 1. What should the modified function do if it finds a file that doesn’t obey this rule?