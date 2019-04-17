### The following code displays a message(s) about the acidity of a solution:

``` python

​ 	ph = float(input(​"Enter the ph level: "​))
​ 	​if​ ph < 7.0:
​ 	    ​print​(​"It's acidic!"​)
​ 	​elif​ ph < 4.0:
​ 	    ​print​(​"It's a strong acid!"​)

```
- What message(s) are displayed when the user enters 6.4?

    - It displays ​ "is acidic."​​

- What message(s) are displayed when the user enters 3.6?

    - It displays ​ "is acidic."​​

- Make a small change to one line of the code so that both messages are displayed 
  when a value less than 4 is entered.

    - We should replace "elif" with just "if". 
      This way there are two "if" both are going to be executed, when "ph" is 4

