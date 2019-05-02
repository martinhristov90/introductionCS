### You are given two lists, rat_1 and rat_2, that contain the daily weights of two rats over a period of ten days. Assume the rats never have exactly the same weight. Write statements to do the following:

rat_waight1 = [1.2,1.5,1.3,1.4,1.4,1.4,1.6,1.3,1.2,1.3]
rat_waight2 = [2.2,2.5,2.3,2.4,2.4,2.4,2.6,2.3,2.2,2.3]


- If the weight of rat 1 is greater than that of rat 2 on day 1, print "Rat 1 weighed more than rat 2 on day 1."; otherwise, print "Rat 1 weighed less than rat 2 on day 1.".

```python

rat_waight1 = [1.2,1.5,1.3,1.4,1.4,1.4,1.6,1.3,1.2,1.3]
rat_waight2 = [2.2,2.5,2.3,2.4,2.4,2.4,2.6,2.3,2.2,2.3]

if rat_waight1[0] > rat_waight2[0]:
    print("Rat 1 weighed more than rat 2 on day 1")
else:
    print("Rat 1 weighed less than rat 2 on day 1.")

```

- If rat 1 weighed more than rat 2 on day 1 and if rat 1 weighs more than rat 2 on the last day, print "Rat 1 remained heavier than Rat 2."; otherwise, print "Rat 2 became heavier than Rat 1."

```python

rat_waight1 = [1.2,1.5,1.3,1.4,1.4,1.4,1.6,1.3,1.2,1.3]
rat_waight2 = [2.2,2.5,2.3,2.4,2.4,2.4,2.6,2.3,2.2,2.3]

if rat_waight1[0] > rat_waight2[0] and rat_waight1[-1] > rat_waight2[-1]:
    print("Rat 1 remained heavier than Rat 2")
else:
    print("Rat 2 became heavier than Rat 1")

```

- If your solution to the previous exercise used nested if statements, then do it without nesting, or vice versa.

```python

rat_waight1 = [1.2,1.5,1.3,1.4,1.4,1.4,1.6,1.3,1.2,1.3]
rat_waight2 = [2.2,2.5,2.3,2.4,2.4,2.4,2.6,2.3,2.2,2.3]

if rat_waight1[0] > rat_waight2[0]:
    if rat_waight1[-1] > rat_waight2[-1]:
        print("Rat 1 remained heavier than Rat 2")
else:
    print("Rat 2 became heavier than Rat 1")

```