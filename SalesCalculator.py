import numpy as np

# sales calculator
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
sales = []

print("Enter the amount of sales for each month in Rupiah")
for month in months:
    value = float(input(f"{month}: Rp "))
    sales.append(value)

sales = np.array(sales)
totalSales = np.sum(sales)
avgSales = np.mean(sales)
highest_sales = np.max(sales)
highest_month = months[np.argmax(sales)]
lowest_sales = np.min(sales)
lowest_month = months[np.argmin(sales)]

print("\n-----========== RESULT ==========-----")
print(f"Total Sales of the Year: Rp {totalSales:,.2f}")
print(f"Average Monthly Sales: Rp {avgSales:,.2f}")
print(f"Highest Sales: Rp {highest_sales:,.2f} at {highest_month}")
print(f"Lowest Sales: Rp {lowest_sales:,.2f} at {lowest_month}")
print("-----============================-----")