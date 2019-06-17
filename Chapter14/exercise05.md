Consider this code:
```python
>>> segment = LineSegment(Point(1, 1), Point(3, 2))
>>> segment.slope()
0.5
>>> segment.length()
2.23606797749979
```
In this exercise, you will write two classes, Point and LineSegment, so that you can run this code and get the same results.

1. Write a Point class with an __init__ method that takes two numbers as parameters.

2. In the same file, write a LineSegment class whose constructor takes two Points as parameters. The first Point should be the start of the segment.

3. Write a slope method in the class LineSegment that computes the slope of the segment. (Hint: The slope of a line is rise over run.)

4. Write a length method in class LineSegment that computes the length of the segment. (Hint: Use x ** n to raise x to the nth power. To compute the square root, raise a number to the (1/2) power or use math.sqrt.)

## Answers to both sub tasks :
```python
import math

class Point:

    def __init__(self,Xaxis,Yaxis):
        self.Xaxis = Xaxis
        self.Yaxis = Yaxis

class LineSegment:

    def __init__(self,segmentStart: Point,segmentEnd: Point):
        self.segmentStart = segmentStart
        self.segmentEnd = segmentEnd

    def slope(self):
        result = (self.segmentStart.Xaxis - self.segmentEnd.Xaxis) / (self.segmentStart.Yaxis - self.segmentEnd.Yaxis)
        return result

    def length(self):
        # Source used : https://www.purplemath.com/modules/distform.htm
        distance = math.sqrt( pow((self.segmentStart.Xaxis - self.segmentEnd.Xaxis),2) + pow((self.segmentStart.Yaxis - self.segmentEnd.Yaxis),2 ))
        return distance
```