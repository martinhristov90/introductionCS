### A sparse vector is a vector whose entries are almost all zero, like [1, 0, 0, 0, 0, 0, 3, 0, 0, 0]. Storing all those zeros in a list wastes memory, so programmers often use dictionaries instead to keep track of just the nonzero entries. For example, the vector shown earlier would be represented as {0:1, 6:3}, because the vector it is meant to represent has the value 1 at index 0 and the value 3 at index 6.

- The sum of two vectors is just the element-wise sum of their elements. For example, the sum of [1, 2, 3] and [4, 5, 6] is [5, 7, 9]. Write a function called sparse_add that takes two sparse vectors stored as dictionaries and returns a new dictionary representing their sum.

    > Answer :
    ```python
        def sparse_add (inDict,inDict1):

            finalDict = {}

            for i in inDict.keys():
                finalDict[i] = inDict[i] + inDict1[i]

            return finalDict

        testDict = {1:1 , 2:2 , 3:3}
        testDict1 = {1:4 , 2:5, 3:6}

        # How to use it :

        print(sparse_add(testDict,testDict1))
    ```


- The dot product of two vectors is the sum of the products of corresponding elements. For example, the dot product of [1, 2, 3] and [4, 5, 6] is 4+10+18, or 32. Write another function called sparse_dot that calculates the dot product of two sparse vectors.

    > Answer :
    ```python

        def sparse_dot (inDict,inDict1):
        
            finalDict = {}
            returnVar = 0

            for i in inDict.keys():
                finalDict[i] = inDict[i] * inDict1[i]

            for item in finalDict.values():
                returnVar = returnVar + item

            return returnVar

        testDict = {1:1 , 2:2 , 3:3}
        testDict1 = {1:4 , 2:5, 3:6}

        # How to use it :

        print(sparse_dot(testDict,testDict1))
    ```

- Your boss has asked you to write a function called sparse_len that will return the length of a sparse vector (just as Python’s len returns the length of a list). What do you need to ask her before you can start writing it?

    > Answer :
    ```python
    
    ```