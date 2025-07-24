A simple webapp to add bank transactions to for budgeting or just general info.

<h1> Features </h1>
<ul>
  <li>Add spendings using a CSV file export from bank</li>
  <li>CSV files with custom ordering of fields is supported</li>
  <li>Check transactions in a list</li>
  <li>View/Edit singular transaction</li>
  <li>Search for transactions between dates and by description</li>
  <li>View Accounts</h1>
  <li>Add / Edit Accounts</li>
  <li>Add / Sort Transactions by category</li>
</ul>
<img width="1680" height="924" alt="Screenshot 2025-07-24 at 13 11 41" src="https://github.com/user-attachments/assets/35bee179-918f-4ff1-b951-c4ec4d0e650d" />
<img width="1676" height="940" alt="Screenshot 2025-07-24 at 13 12 01" src="https://github.com/user-attachments/assets/bca35d15-642e-41ae-879d-d990ef0a7941" />

<h1> How to Run </h1>
Make sure to install python 3.12 and django 5.1.1.

Open terminal at main folder location.

For the first time run:<br>
<code> python3 manage.py migrate </code>

To start up the server run:<br>
<code> python3 manage.py runserver </code>

The webapp can then be accessed from 127.0.0.1:8000 or localhost:8000

<h3> Disclaimer </h3>
This is still a test version and so django will display verbose error screens if there is an error.
I have also only tested this on my laptop and it works fine for my use case, however this may not work on your machine, if this doesn't work I will try my best to help so feel free to raise an issue.
