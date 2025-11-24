

# Smart Bill Splitter & Expense Tracker

 

##  Overview

The **Smart Bill Splitter & Expense Tracker** is a lightweight, Python-based command-line interface (CLI) tool designed to simplify financial management for friends and individuals.

It solves two common problems:

1.  Splitting restaurant bills or shared costs (including tax and tips) without the math headache.
2.  Tracking personal expenses and saving them to a persistent history file.

Whether you are splitting a pizza with friends or buying a bus ticket for yourself, this tool saves your share directly to a local history file (`my_expenses.txt`) with a timestamp.

-----

##  Features

  * ** Smart Bill Splitting:**
      * Calculate total bills including tax/tip percentages.
      * **Split Equally:** Divides the total evenly among all participants.
      * **Split by Item:** Allows entering specific amounts for each person (great for when someone only ordered a salad and someone else ordered a steak).
  * ** Personal Expense Logging:** Quickly add individual purchases to your record.
  * ** Persistent History:** Automatically saves date, description, and amount to `my_expenses.txt`.
  * ** Currency Support:** Full support for the Indian Rupee symbol (₹) using UTF-8 encoding.
  * ** Error Handling:** Safely handles file creation and reading (checks if the history file exists before reading).

-----

##  Technologies & Tools Used

  * **Language:** Python 3.x
  * **Libraries:**
      * `os` (File path management)
      * `datetime` (Timestamping expenses)
  * **Storage:** Text file (`.txt`) for lightweight, readable data storage.

-----

##  Steps to Install & Run

### Prerequisites

Ensure you have **Python 3** installed on your system. You can check this by running:

```bash
python --version
```

### Installation

1.  **Download the code:** Save the Python script provided into a file named `expense_tracker.py`.
2.  **Open your terminal/command prompt.**
3.  **Navigate to the folder** where you saved the file.

### Running the Project

Execute the script using the following command:

```bash
python expense_tracker.py
```

-----

##  Instructions for Testing

Follow these scenarios to test if the application is working correctly:

### Test Case 1: Splitting a Bill

1.  Run the script and select **Option 1** (Split a Bill).
2.  Enter a total amount (e.g., `1000`).
3.  Enter a tax/tip percentage (e.g., `5`).
4.  Choose to split **Equally**.
5.  When prompted, type `y` to save **your** share to history.
6.  *Expected Output:* The script calculates the split and confirms the data is saved.

### Test Case 2: Adding a Personal Expense

1.  Select **Option 2** (Add a Personal Expense).
2.  Enter a description (e.g., "Coffee") and amount (e.g., "150").
3.  *Expected Output:* A confirmation message saying the expense was saved.

### Test Case 3: Viewing History

1.  Select **Option 3** (View My Expense History).
2.  *Expected Output:* You should see a list of the expenses you added in the previous steps, formatted with today's date and the `₹` symbol.

-----

##  Project Structure

```text
├── expense_tracker.py    # The main application script
├── my_expenses.txt       # Automatically generated file storing your history
└── README.md             # Project documentation
```
