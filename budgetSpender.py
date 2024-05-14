import pandas as pd
import matplotlib.pyplot as plt

# Initialize data storage
data = {
    'Month': [],
    'Income': [],
    'Expenses': []
}

def add_financials(month, income, expenses):
    for key in list(data.keys()):
        if key not in ['Month', 'Income', 'Expenses'] and key not in expenses:
            expenses[key] = 0  # Assign zero if no expense for this category in the current month

    data['Month'].append(month)
    data['Income'].append(income)
    total_expenses = sum(expenses.values())
    data['Expenses'].append(total_expenses)
    for expense, amount in expenses.items():
        if expense in data:
            data[expense].append(amount)
        else:
            data[expense] = [0] * (len(data['Month']) - 1)  # Pad previous months with zeros
            data[expense].append(amount)

def input_financials():
    while True:
        month = input("Enter the month (e.g., January, February, etc.): ")
        if month.capitalize() in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
            break
        print(f"That is not a valid month. Can you try again?")
    
    while True:
        try:
            income = float(input("Enter total income for the month: "))
            break
        except ValueError:
            print("That is not a valid amount. Please enter a numeric value.")

    expenses = {}
    while True:
        expense_item = input("Enter an expense category or type 'done' to finish: ")
        if expense_item.lower() == 'done':
            break
        while True:
            try:
                expense_amount = float(input(f"Enter amount for {expense_item}: "))
                break
            except ValueError:
                print("That is not a valid amount. Please enter a numeric value.")
        expenses[expense_item] = expense_amount
    add_financials(month, income, expenses)

def plot_financials():
    df = pd.DataFrame(data)
    for month in df['Month'].unique():
        monthly_data = df[df['Month'] == month]
        expenses = monthly_data.drop(['Month', 'Income', 'Expenses'], axis=1).iloc[0]
        plt.figure(figsize=(8, 6))
        plt.title(f'Expenses for {month}')
        plt.pie(expenses, labels=expenses.index, autopct='%1.1f%%', startangle=140)
        plt.show()

def save_to_excel():
    df = pd.DataFrame(data)
    df.to_excel('budget_tracker.xlsx', index=False)
    print("Data saved to 'budget_tracker.xlsx'.")

# User input loop
number_of_months = int(input("How many months of data do you want to enter? "))
for _ in range(number_of_months):
    input_financials()

# Plotting and saving the financial data
plot_financials()
save_to_excel()
