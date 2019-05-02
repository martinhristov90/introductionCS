### You want an automatic wildlife camera to switch on if the light level is less than 0.01 lux 
### or if the temperature is above freezing, but not if both conditions are true. 
### (You should assume that function turn_camera_on has already been defined.)

- Your first attempt to write this is as follows:
```python
​ 	​if​ (light < 0.01) ​or​ (temperature > 0.0):
​ 	    ​if​ ​not​ ((light < 0.01) ​and​ (temperature > 0.0)):
​ 	        turn_camera_on()
```
-  A friend says that this is an exclusive or and that you could write it more simply as follows:
```python
​ 	​if​ (light < 0.01) != (temperature > 0.0):
​ 	    turn_camera_on()
```
-  Is your friend right? If so, explain why. If not, give values for light and temperature that will produce different results for the two fragments of code.