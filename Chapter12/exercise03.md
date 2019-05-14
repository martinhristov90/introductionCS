### In ​The Readline Technique​, you learned how to read some files from the Time Series Data Library. In particular, you learned about the Hopedale data set, which describes the number of colored fox fur pelts produced from 1834 to 1842. This file contains one value per year per line.



- Write an outline in English of the algorithm you would use to read the values from this data set to compute the average number of pelts produced per year.
    Answer :
    - readline() function should be applied to the file descriptor, it moves the cursor to the beggining of the nextline.
    - The line that that is read by readline(), should be store in variable.
    - If the line starts with '#' it should be discated, until we read the first line of data.
    - When we have the first line of real data, we can iterate over the rest of the line till the end of the file.
    - Those values needs to be stripped from any chars and casted to int() and sum up with for loop.

- Translate your algorithm into Python by writing a function named hopedale_average that takes a filename as a parameter and returns the average number of pelts produced per year.
    ```python
    
    from typing import TextIO

    def hopedale_average(inFile: TextIO) -> float:
        with open(inFile,'r') as fd :

            fd.readline()
            data = fd.readline().strip()

            while data.startswith('#'):
                data = fd.readline().strip()

            total_pelts = int(data)

            numOfPelts = 1

            for data in fd:
                total_pelts = total_pelts + int(data.strip())
                numOfPelts = numOfPelts + 1

        return total_pelts/numOfPelts


    print(hopedale_average('data.txt'))

    ```