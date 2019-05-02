### In  Processing Whitespace-Delimited Data , we used the “For Line in File” technique to process data line by line, breaking it into pieces using string method split. Rewrite function process_file to skip the header as normal but then use the Read technique to read all the data at once.

- Processing Whitespace-Delimited Data 

```python

from  typing  import  TextIO
from  io  import  StringIO
import  time_series
    
def  process_file(reader: TextIO) -> int:

    """Read and process reader, which must start with a time_series header. 
    Return the largest value after the header.  There may be multiple pieces 
    of data on each line. 
    >>> infile = StringIO('Example \\ n 20. 3. \\ n 100. 17. 15. \\ n') 
    >>> process_file(infile) 
    100 
    """ 
   line = time_series.skip_header(reader).strip()
    # The largest value so far is the largest on this first line of data. 
   largest = find_largest(line)
    # To read the rest of the date at one, read() should be used, it keeps on reading until encounters EOF .
    text = reader.read()
    print(text)

if  __name__ ==  '__main__' :
    with  open( 'lynx.txt' ,  'r' )  as  input_file:
        print (process_file(input_file))

```