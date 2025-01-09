<center>
[![](---ThisDir---/sb.jpg)](https://youtu.be/Az49aNuYeJs?si=8tOncILA2YeXal0U)
</center>

<center>
*...exceptions...*
</center>

<center>
**A**
</center>

<center>
(2 points)
</center>

Write a simple calendar application. The calendar events are written to a text file
with the following style of syntax:

```
...
python for beginners @ 2025-01-10 16:00-18:30 
lunch @ 2025-01-11 12:00-13:00 
...
```

The application has a simple programming interface. Given a day:


```
$ python myCalendarAll.py 2025-01-11
```

it returns a list of events and for that day in a nicely formatted table with the hours
in a separate column.   

Use exceptions and exception chaining when reading the calendar file.
If there is a syntax error in the file - gracefully handle the situation.
Don't crash the program, provide the user with information about the error
(line number for example) so the problem could be fixed.

Tip: Use the `split` method for strings and, for now, `ValueError` exceptions.
Use the `argparse` library to create a command line interface.

<center>
**B**
</center>

<center>
(3 points)
</center>

Write custom exceptions to handle the following potential problems in **A**:

- badly formatted date
- badly formatted time
- no date specified
- no time specified

Gracefully handle each of these exceptions in the code.

<center>
**C**
</center>

<center>
(3 points)
</center>

Create a base class `CalendarEvent` with the following methods:

- `getDate` returns a string with the date for the time of the calendar event
- `getTime` returns a string with the time for the calendar event
- `getDescription` returns a string with the description of the calendar event
- `getRow` returns a elegantly formated string with information about the event

Next create three child classes:

- `EventWithTimeAndDate`
- `EventWithDateAndNoTime`
- `EventWithTimeAndNoDate`

That hande the situations described by their name.



