import csv

# -------------------------
# 1️⃣ Load Expenses
# -------------------------


def load_expenses(filename):
    """
    CSV file থেকে expenses load করবে।
    Return: list of dict
    """
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                # amount কে int বা float এ convert করো
                data.append({
                    "date": row["date"],
                    "category": row["category"],
                    "amount": float(row["amount"])
                })
            return data
    except FileNotFoundError:
        print("File not found")
        return []


# -------------------------
# 2️⃣ Add Expense
# -------------------------
def add_expense(expense_list, date, category, amount):
    """
    নতুন expense add করবে
    """
    # এখানে নতুন dict append করো
    pass  # ✅ Fill this


# -------------------------
# 3️⃣ Category-wise Total
# -------------------------
def category_summary(expense_list):
    """
    Category-wise total calculate করবে
    Return: dict
    """
    summary = {}
    # summary[category] = summary.get(category,0) + amount
    pass  # ✅ Fill this
    return summary


# -------------------------
# 4️⃣ Monthly Report
# -------------------------
def monthly_report(expense_list, month="01"):
    """
    শুধু নির্দিষ্ট মাসের total দেখাবে
    month format: "01", "02", ..., "12"
    Return: total_amount
    """
    total = 0
    # date split করে month বের করে add করো
    pass  # ✅ Fill this
    return total


# -------------------------
# 5️⃣ Save Report
# -------------------------
def save_report(filename, summary):
    """
    Report text file এ save করবে
    """
    with open(filename, "w") as file:
        file.write("Expense Summary Report\n")
        file.write("-"*30 + "\n")
        for category, amount in summary.items():
            file.write(f"{category}: {amount}\n")
    print(f"Report saved as {filename}")


# -------------------------
# MAIN FLOW
# -------------------------
expenses = load_expenses("expense.csv")
print(expenses)
# Test: নতুন expense add করা
# add_expense(expenses, "2026-01-20", "Food", 350)

category_totals = category_summary(expenses)
print("Category-wise total:", category_totals)

january_total = monthly_report(expenses, "01")
print("Total expense in January:", january_total)

# Save report
save_report("expense_report.txt", category_totals)
