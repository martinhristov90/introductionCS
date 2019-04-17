### In the following exercises, you will work with Python’s calendar module:

    1. Visit the Python documentation website at http://docs.python.org/release/3.6.0/py-modindex.html, and look at the  documentation on module calendar.
    2. Import module calendar.
    3. Using function help, read the description of function isleap.
    4. Use isleap to determine the next leap year.
    5. Use dir to get a list of what calendar contains.
    6. Find and use a function in module calendar to determine how many leap years there will be between the years 2000 and 2050, inclusive.
    7. Find and use a function in module calendar to determine which day of the week July 29, 2016, will be.

- 1. I visited the website and looked up the documentation on calendar module.

- 2. We need to use the import statement like this:
    ```python
    import calendar
    ```
- 3. I used help(calendar.isleap)
    ```python
    >>> help(calendar.isleap)
    Help on function isleap in module calendar:

    isleap(year)
        Return True for leap years, False for non-leap years.
    >>> 
    ```
- 4. Determining the next leap year, it would be year 2020 :
    ```python
    >>> calendar.isleap(2020)
    True
    >>>  
    ```
- 5. Using the built-in function dir() to look up items contained in "calendar" module.
    ```python
    >>> dir(calendar)
    ['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY',    'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',   '__spec__', '_colwidth', '_locale', '_localized_day', '_localized_month', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday',   'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthlen', 'monthrange', 'nextmonth', 'prcal', 'prevmonth',   'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']
    >>> 
    ```
- 6. I'm going to use the function calendar.leapdays() :
    ```python
    >>> help(calendar.leapdays)
    Help on function leapdays in module calendar:

    leapdays(y1, y2)
        Return number of leap years in range [y1, y2).
        Assume y1 <= y2.
    >>> calendar.leapdays(2000,2050)
    13
    >>> 
    ```
- 7. I'm going to use the function calendar.weekday(), 29th of July 2016 has been Friday :
    ```python
    >>> help(calendar.weekday)
    Help on function weekday in module calendar:
    weekday(year, month, day)
    Return weekday (0-6 ~ Mon-Sun) for year, month (1-12), day (1-31).
    >>> calendar.weekday(2016, 7, 29)
    4
    >>> 
