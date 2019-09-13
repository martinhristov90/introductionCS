### In this exercise, you will create a table to store the population and land area of the Canadian provinces and territories according to the 2001 census. Our data is taken from http://www12.statcan.ca/english/census01/home/index.cfm.

1. Creates a new database called census.db

```python
import sqlite3 as dbapi
con = dbapi.connect('census.db')
```

2. Makes a database table called Density that will hold the name of the province or territory (TEXT), the population (INTEGER), and the land area (REAL).

```python
cur = con.cursor()

cur.execute('''CREATE TABLE Density(Province TEXT,Population INTEGER, Area REAL ''')
con.commit()
```

3. Inserts the data from Table 34, 2001 Canadian Census Data

```python
table = [
 ('Newfoundland and Labrador', 512930, 370501.69),
 ('Prince Edward Island', 135294, 5684.39),
 ('Nova Scotia', 908007, 52917.43),
 ('New Brunswick', 729498, 71355.67),
 ('Quebec', 7237479, 1357743.08),
 ('Ontario', 11410046, 907655.59),
 ('Manitoba', 1119583, 551937.87),
 ('Saskatchewan', 978933, 586561.35),
 ('Alberta', 2974807, 639987.12),
 ('British Columbia', 3907738, 926492.48),
 ('Yukon Territory', 28674, 474706.97),
 ('Northwest Territories', 37360, 1141108.37),
 ('Nunavut', 26745, 1925460.18),
]

for row in table:
    cur.execute('INSERT INTO Density VALUES (?, ?, ?)', row)
con.commit()
```

4. Retrieves the contents of the table

```python
cur.execute('SELECT * FROM Density')

for row in cur.fetchall():
    print(row)
```

5. Retrieves the populations

```python
cur.execute('SELECT Population FROM Density')

for row in cur.fetchall():
    print(row)
```

6. Retrieves the provinces that have populations of less than one million

```python
cur.execute('''SELECT Province FROM Density WHERE Population < 1000000''')
for row in cur.fetchall():
    print(row)
```

7. Retrieves the provinces that have populations of less than one million or greater than five million

```python
cur.execute('''SELECT Province FROM Density WHERE Population < 1000000 OR Population > 5000000''')
for row in cur.fetchall():
    print(row)
```

8. Retrieves the provinces that do not have populations of less than one million or greater than five million

```python
cur.execute('''SELECT Province FROM Density WHERE NOT(Population < 1000000 OR Population > 5000000)''')
for row in cur.fetchall():
    print(row)
```

9. Retrieves the populations of provinces that have a land area greater than 200,000 square kilometers

```python
cur.execute('''SELECT Population FROM Density WHERE Area > 200000''')
for row in cur.fetchall():
    print(row)
```

10. Retrieves the provinces along with their population densities (population divided by land area)

```python
cur.execute('SELECT Province, Population / Area FROM Density')
for row in cur.fetchall():
    print(row)
```