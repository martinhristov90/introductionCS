### Your job is to come up with tests for a function called line_intersect, which takes two lines as input and returns their intersection. More specifically:

- Lines are represented as pairs of distinct points, such as [[0.0,0.0], [1.0, 3.0]] .

- If the lines don’t intersect, line_intersect returns None.

- If the lines intersect in one point, line_intersect returns the point of intersection, such as [0.5, 0.75].

- If the lines are coincident (that is, lie on top of each other), the function returns its first argument (that is, a line).

What are the six most informative test cases you can think of? (That is, if you were allowed to run only six tests, which would tell you the most about whether the function was implemented correctly?)

Write out the inputs and expected outputs of these six tests, and explain why you would choose them.

### Answer : 

- Both of the lines lie on top of each other :
```python
[[1.0,2.0], [2.0,3.0],[1.0,2.0], [2.0,3.0]]
```
This should return a first argument, a line !
- The first argument ([1.0,1.0], [1.0,1.0]) represents a point, not a line, the second argument ([2.0,2.0], [3.0,3.0]) is a line, intersection is not possible :
```python
[[1.0,1.0], [1.0,1.0],[2.0,2.0], [3.0,3.0]]
```
- Vice versa :
```python
[[2.0,2.0], [3.0,3.0],[1.0,1.0], [1.0,1.0]]
```
- Two lines intersect at one point : 
```python
[[1.0,2.0], [3.0,3.0],[2.0,1.0], [2.0,4.0]]
```
- When lines do not intersect, but both arguments represent a line :
```python
[[1.0,1.0], [2.0,2.0],[3.0,3.0], [4.0,4.0]]
```
- When the end of the first line is the start of the second line:
```python
[[1.0,1.0], [2.0,2.0],[2.0,2.0], [3.0,3.0]]
```