### Function convert_to_celsius from ​Defining Our Own Functions​, converts from Fahrenheit to Celsius. Wikipedia, 
### however, discusses eight temperature scales: Kelvin, Celsius, Fahrenheit, Rankine, Delisle, Newton, Rèaumur, and 
### Rømer. Visit http://en.wikipedia.org/wiki/Comparison_of_temperature_scales to read about them.

- Write a convert_temperatures(t, source, target) function to convert temperature t from source units to target units, where source and target are each one of "Kelvin", "Celsius", "Fahrenheit", "Rankine", "Delisle", "Newton", "Reaumur", and "Romer" units.

    Hint: On the Wikipedia page there are eight tables, each with two columns and seven rows. That translates to an awful lot of if statements—at least 8 * 7—because each of the eight units can be converted to the seven other units. Possibly even worse, if you decided to add another temperature scale, you would need to add at least sixteen more if statements: eight to convert from your new scale to each of the current ones and eight to convert from the current ones to your new scale.

    A better way is to choose one canonical scale, such as Celsius. Your conversion function could work in two steps: convert from the source scale to Celsius and then from Celsius to the target scale.

- Now if you added a new temperature scale, how many if statements would you need to add?

