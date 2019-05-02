### Modify the file reader in read_smallest_skip.py of ​Skipping the Header​, so that it uses a continue inside the loop instead of an if. Which form do you find easier to read?

```python

from  typing  import  TextIO
from  io  import  StringIO
import  time_series

def  smallest_value_skip(reader: TextIO) -> int:
    """Read and process reader, which must start with a time_series header. 
    Return the smallest value after the header.  Skip missing values, which 
    are indicated with a hyphen. 
    >>> infile = StringIO('Example  \\  n1  \\  n-  \\  n3  \\  n') 
    >>> smallest_value_skip(infile) 
    1 
    """ 
   line = time_series.skip_header(reader).strip()
    # Now line contains the first data value; this is also the smallest value 
    # found so far, because it is the only one we have seen. 
    

    smallest = int(line)
    for  line  in  reader:
       line = line.strip()
        if  line !=  '-' :
            continue
        value = int(line)
        smallest = min(smallest, value)
    return  smallest

        
if  __name__ ==  '__main__' :
    with  open( 'hebron.txt' ,  'r' )  as  input_file:
        print (smallest_value_skip(input_file))
