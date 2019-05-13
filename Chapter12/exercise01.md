### A DNA sequence is a string made up of the letters A, T, G, and C. To find the complement of a DNA sequence, As are replaced by Ts, Ts by As, Gs by Cs, and Cs by Gs. For example, the complement of AATTGCCGT is TTAACGGCA.

- Write an outline in English of the algorithm you would use to find the complement.

    > Answer :
    > In order to substitute the letters, we need to go over each one and replace it with the appropriate one.

- Review your algorithm. Will any characters be changed to their complement and then changed back to their original value? If so, rewrite your outline. Hint: Convert one character at a time, rather than all of the As, Ts, Gs, or Cs at once.

    > Answer :
    > Let's take 'A's and 'T's, those characters are located on different possitions, so the answer would be no.

- Using the algorithm that you have developed, write a function named complement that takes a DNA sequence (a str) and returns the complement of it.
    ```python
    
    def compliment(inVar: str) -> str:

        retStr = []
        for i in inVar:
            if i == 'A':
                retStr.append('T')
            if i == 'T':
                retStr.append('A')
            if i == 'G':
                retStr.append('C')
            if i == 'C':
                retStr.append('G')

    print("".join(str(char) for char in retStr))

    # How to use it :

    compliment('AATTGCCGT')

    ```

    
