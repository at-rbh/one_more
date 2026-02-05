import csv
from datetime import datetime

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
    expense_list.append({
        "date": date,
        "category": category,
        "amount": float(amount)
    })
    return expense_list


# -------------------------
# 3️⃣ Category-wise Total
# -------------------------


def category_summary(expense_list):
    """
    Category-wise total calculate করবে
    Return: dict
    """
    summary = {}
    for item in expense_list:
        summary[item["category"]] = summary.get(
            item["category"], 0) + item["amount"]

    return summary


# -------------------------
# 4️⃣ Monthly Report
# -------------------------
def monthly_report(expense_list, month=1):
    """
    শুধু নির্দিষ্ট মাসের total দেখাবে
    month format: "01", "02", ..., "12"
    Return: total_amount
    """
    months = ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]

    total = 0
    # date split করে month বের করে add করো
    for item in expense_list:
        month_no = int(item['date'].split("-")[1])
        if month_no == month:
            total += item["amount"]
    return total, months[month - 1]


def highest_expense_category(summary):

    return max(summary.items(), key=lambda x: x[1])


def highest_expense_day(expense_list):
    date_total = {}

    for item in expense_list:
        date_total[item["date"]] = date_total.get(
            item["date"], 0) + item["amount"]
    return max(date_total.items(), key=lambda item: item[1])


# -------------------------
# 5️⃣ Save Report
# -------------------------
def save_report(filename, summary, report):
    """
    Report text file এ save করবে
    """

    with open(filename, "w") as file:
        file.write("Expense Summary Report\n")
        file.write("-"*30 + "\n")
        for category, amount in summary.items():
            file.write(f"{category}: {amount}\n")

        file.write(f"\nTotal expense in {report['month_report'][1]}:\n")
        file.write("-"*30 + "\n")
        file.write(
            f"Total expense in {report['month_report'][1]}: {report['month_report'][0]}")
        file.write(f"\nHighest expense category {report['highest_ctg'][1]}:\n")
        file.write("-"*30 + "\n")
        file.write(
            f"\nHighest expense day in {report['highest_day'][0]}: {report['highest_day'][1]}\n")
        file.write("-"*30 + "\n")
    print(f"Report saved as {filename}")


# -------------------------
# MAIN FLOW
# -------------------------
expenses = load_expenses("expense.csv")
print(expenses)
# Test: নতুন expense add করা
add_expense(expenses, "2026-02-20", "Food", 350)

category_totals = category_summary(expenses)
print("Category-wise total:", category_totals)

month_report = monthly_report(expenses, 2)
print(f"Total expense in {month_report[1]}:", month_report[0])


highest_ctg = highest_expense_category(category_totals)
highest_day = highest_expense_day(expenses)

report = {
    "month_report": month_report,
    "highest_ctg": highest_ctg,
    "highest_day": highest_day
}

# Save report
save_report("expense_report.txt", category_totals, report)
