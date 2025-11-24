
***

# Project Statement: Smart Bill Splitter & Tracker

## 1. Problem Statement
In social settings, splitting bills among friends is often a hassle, especially when adding tax or tips and accounting for individual orders. Furthermore, individuals often struggle to maintain a centralized record of both their daily personal expenses and their share of group expenditures. Manual calculations are error-prone, and using separate tools for calculation and tracking leads to fragmented financial records.

## 2. Scope of the Project
This project is a command-line interface (CLI) application designed to combine a bill calculator with a personal expense tracker.
* **In Scope:**
    * Calculating total bill amounts including customizable tax/tip percentages.
    * Splitting bills equally among a group or calculating individual shares based on consumption.
    * Logging personal daily expenses.
    * Saving the user's specific share of a group bill to their personal history.
    * Persistent storage of data using a local text file (`my_expenses.txt`).
* **Out of Scope:**
    * Graphical User Interface (GUI) or Mobile App features.
    * Complex data analytics or graphical visualizations.
    * Cloud synchronization or multi-user remote access.

## 3. Target Users
* **Students and Roommates:** Who frequently share expenses for meals, utilities, or outings.
* **Groups of Friends:** Who dine out often and need a quick way to calculate tips and split costs fairly.
* **Budget-Conscious Individuals:** Who want a simple, no-frills text record of where their money is going without complex banking apps.

## 4. High-Level Features
* **Dual-Mode Bill Splitter:**
    * **Equal Split:** Automatically divides the total (including tax/tip) by the number of people.
    * **Itemized Split:** Allows inputting specific amounts for each person (for cases where orders vary in price), calculating their specific tax/tip share automatically.
* **Tax & Tip Calculator:** Accepts a custom percentage input to automatically adjust total totals before splitting.
* **Personal Expense Logger:** A quick entry system to record daily purchases (e.g., bus tickets, coffee) with timestamps.
* **Integrated History Saving:** The ability to seamlessly save the user's specific calculated share from a group bill directly into their personal expense history.
* **Expense History Viewer:** A read-function that retrieves and displays all past recorded transactions with dates and descriptions.

---

