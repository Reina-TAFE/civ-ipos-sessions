# Remember you file paths when you attempt use this file reader
# import the reuseable csv library - docs at: https://docs.python.org/3/library/csv.html
import csv
# Function to read data from CSV file
def read_sales_data(filename):
    sales_data = []
    # Task 1: Read data from CSV file
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["Product Name"] = row["Product"]
            row["Units Sold"] = row["Units Sold"]
            row["Unit Price"] = row["Unit Price"]
            row["Total Revenue"] = row["Total Revenue"]
            sales_data.append(row)
        return sales_data

sales_data = read_sales_data("sales_data.csv")
# Task 2: Calculate total revenue for each product
product_revenue = {}
for product in sales_data:
    product_revenue[product["Product Name"]] = (product["Units Sold"] * product["Unit Price"])

# Task 3: Identify the product with the highest total units sold
max_units_sold = list(filter(lambda product: sales_data[product]["Units Sold"] == max(sales_data), range(len(sales_data))))[0][0]
# Task 4: Calculate average unit price for each product - watch out for division by zero



# Display results
print("Total revenue for each product:")
for product, revenue in product_revenue.items():
    print(f"{product}: ${revenue:.2f}")

print("\nThe product with the highest total units sold:")
print(max_units_sold_product)

print("\nAverage unit price for each product:")
for product, avg_price in product_unit_price.items():
    print(f"{product}: ${avg_price:.2f}")