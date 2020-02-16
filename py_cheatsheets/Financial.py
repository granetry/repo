import numpy as np
import matplotlib.pyplot as plt


# Dictionaries containing information for expense categories
Needs = {"Rent": 350.00, "Utilities": 60.00, "Food": 60.00,
         "Car": 0.00, 'Gym': 10.00, 'Car Insurance': 0}
Wants = {'OSRS': 20.48, 'Spotify': 9.99, 'Hulu': 5.99, 'Chegg': 14.95}
Debts = {'CreditOne': 25.00, 'Capital_OneA': 25.00, 'Capital_OneB': 25.00, 'BestBuy': 50.00}

# Sum of each dictionary
Needs_Amt = sum(Needs.values())
Wants_Amt = sum(Wants.values())
Debts_Amt = sum(Debts.values())

# Total sum of expenses
Total_Liability = sum(Needs.values()) + sum(Wants.values()) + sum(Debts.values())

# Layout of income source and total sum of income.
Income_Source = {"LCC": 312.00, "MSU": 250}
Income = sum(Income_Source.values()) * 2

# Save additional income, after expenses, as a sum and a percentage.
Savings = round(((Income - Total_Liability) / Income) * 100, 2)
Savings_Amt = Income - Total_Liability

# Expense categories as a fraction of total income
Needs_Percent = round(sum(Needs.values()) / Income, 2) * 100
Debt_Percent = round(sum(Debts.values()) / Income, 2) * 100
Wants_Percent = round(sum(Wants.values()) / Income, 2) * 100

###########################################
# Create lists to hold values for visuals #
###########################################

# y_thresh represents percentage points of desired budgetting plan
y_thresh = [50, 30, 10, 10]

# y_sum holds the sum of categories along side total income
y_sum = [Income, Total_Liability, Needs_Amt, Wants_Amt, Debts_Amt, Savings_Amt]

# y_perc holds the values of percentage points
y_perc = [Needs_Percent, Wants_Percent, Debt_Percent, Savings]

# Perc_Cat represents the categories for percentage-based visuals
# Sum_Cat represents the categories for sum-based visuals
Perc_Cat = ['Needs', 'Wants', 'Debts', 'Savings']
Sum_Cat = ['Income', 'Liabilities', 'Needs', 'Wants', 'Debts', 'Savings']

# Load_Out will give a quick numerical breakdown of budget


def Load_Out(x=1):
    print('LOADOUT --- Needs: {}%, Wants: {}, Debts: {}%, and Savings: {}%.'.format(
        Needs_Percent, Wants_Percent, Debt_Percent, Savings))


def Budget_Sum(x=Sum_Cat, y=y_sum):
    plt.figure(figsize=(10, 7))
    colors = ['green', 'red', 'grey', 'grey', 'grey', 'grey']
    plt.bar(Sum_Cat, y_sum, alpha=0.5, color=colors)
    plt.title('Total Amt (Monthly)', fontsize=20)
    plt.ylabel('USD ($)', fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid(alpha=0.4)


def Budget_Perc(a=Perc_Cat, b=y_thresh, c=y_perc):
    plt.figure(figsize=(10, 7))
    width = 0.3
    x = [0 + 0.142, 1 + 0.142, 2 + 0.142, 3 + 0.142]
    plt.bar(np.arange(len(y_thresh)), y_thresh, width=width, alpha=0.7, label='Rule')
    plt.bar(np.arange(len(y_perc)) + width, y_perc, width=width, alpha=0.7, label='Actual')
    plt.title('50/30/10/10 Budget Breakdown', fontsize=20)
    plt.xticks(x, Perc_Cat)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    plt.ylabel('Percent (%)', fontsize=15)
    plt.grid(alpha=0.5)
    plt.legend()
    plt.show()

# p in fv_oa represents the amount of money added per week.


def fv_oa(p=10, r=0.06, n=10):
    fv_oa = round((p * 12) * ((((1.0 + r) ** n) - 1) / r), 2)
    return fv_oa


Budget_Sum()
Budget_Perc()
Load_Out()
fv_oa()
