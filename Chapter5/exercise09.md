### Assume we want to print a strong warning message if a pH value is below 3.0 
### and otherwise simply report on the acidity. We try this if statement:

```python

​>>>​​ ​​ph​​ ​​=​​ ​​2​
​ 	​>>>​​ ​​if​​ ​​ph​​ ​​<​​ ​​7.0:​
​ 	​...​​     ​​print(ph,​​ ​​"is acidic."​​)​
​ 	​...​​ ​​elif​​ ​​ph​​ ​​<​​ ​​3.0:​
​ 	​...​​     ​​print(ph,​​ ​​"is VERY acidic! Be careful."​​)​
​ 	​...​
​ 	2 is acidic.

```

### This prints the wrong message when a pH of 2 is entered. What is the problem, and how can you fix it?
