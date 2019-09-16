### For this exercise, add a new table called Capitals to the database. Capitals has three columns—province/territory (TEXT), capital (TEXT), and population (INTEGER)—and it holds the data shown here:

1. Retrieve the contents of the table
```python
cur.execute('SELECT * FROM Capitals')
for row in cur.fetchall():
    print(row)
```

2. Retrieve the populations of the provinces and capitals (in a list of tuples of the form [province population, capital population])

```python
cur.execute('''SELECT Density.Population, Capitals.Population FROM Capitals INNER JOIN Density WHERE Capitals.Province = Density.Province''')
for row in cur.fetchall():
    print(row)
```

3. Retrieve the land area of the provinces whose capitals have populations greater than 100,000

```python
cur.execute('''SELECT Density.Area
 FROM Capitals INNER JOIN Density
 WHERE Capitals.Province = Density.Province
 AND Capitals.Population > 100000''')
for row in cur.fetchall():
    print(row)
```

4. Retrieve the provinces with land densities less than two people per square kilometer and capital city populations more than 500,000

```python
cur.execute('''SELECT Density.Province
 FROM Capitals INNER JOIN Density
 WHERE Capitals.Province = Density.Province
 AND Density.Population / Density.Area < 2
 AND Capitals.Population > 500000''')
for row in cur.fetchall():
 print(row)
```

5. Retrieve the total land area of Canada

```python
cur.execute('SELECT SUM(Area) FROM Density')
print(cur.fetchone())
```

6. Retrieve the average capital city population

```python
cur.execute('SELECT AVG(Population) FROM Capitals')
print(cur.fetchone())
```

7. Retrieve the lowest capital city population

```python
cur.execute('SELECT MIN(Population) FROM Capitals')
print(cur.fetchone())
```

8. Retrieve the highest province/territory population

```python
cur.execute('SELECT MAX(Population) FROM Density')
print(cur.fetchone())
```

9. Retrieve the provinces that have land densities within 0.5 persons per square kilometer of on another—have each pair of provinces reported only once

```python
cur.execute('''SELECT A.Province, B.Province
 FROM Density A INNER JOIN Density B
 WHERE A.Province < B.Province
 AND ABS(A.Population / A.Area - B.Population / B.Area) <
0.5''')
for row in cur.fetchall():
    print(row)
```