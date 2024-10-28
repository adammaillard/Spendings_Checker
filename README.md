A simple webapp to add bank transactions to for budgeting or just general info.

<h1> Features </h1>
<h2> Implemented </h2>
<ul>
  <li>Add spendings using a CSV file export from bank</li>
  <li>CSV files with custom ordering of fields is supported</li>
  <li>Check transactions in a list</li>
  <li>View/Edit singular transaction</li>
  <li>Search for transactions between dates and by description</li>
  <li>View Accounts</h1>
</ul>
<h2> Working On </h2>
<ul>
  <li>Add / Edit Accounts</li>
  <li>Add / Sort Transactions by category</li>
</ul>

<h1> How to Run </h1>
Make sure to install python 3.12 and django 5.1.1.

Open terminal at main folder location.

For the first time run:<br>
<code> python3 manage.py migrate </code>

To start up the server run:
<code> python3 manage.py runserver </code>

The webapp can then be accessed from 127.0.0.1:8000 or localhost:8000

<h3> Disclaimer </h3>
This is still a test version and so django will display verbose error screens if there is an error.
I have also only tested this on my laptop and it works fine for my use case, however this may not work on your machine, if this doesn't work I will try my best to help so feel free to raise an issue.
