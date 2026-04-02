import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

months = df['month_number']

plt.plot(months, df['total_profit'], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

plt.plot(months, df['facecream'], label='Face Cream')
plt.plot(months, df['facewash'], label='Face Wash')
plt.plot(months, df['toothpaste'], label='Toothpaste')
plt.plot(months, df['bathingsoap'], label='Bathing Soap')
plt.plot(months, df['shampoo'], label='Shampoo')
plt.plot(months, df['moisturizer'], label='Moisturizer')

plt.title("Sales Data of All Products")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend()
plt.show()

x = range(len(months))

plt.bar(x, df['facecream'], width=0.4, label='Face Cream')
plt.bar([i + 0.4 for i in x], df['facewash'], width=0.4, label='Face Wash')

plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.title("Face Cream vs Face Wash Sales")
plt.legend()
plt.show()

total_sales = [
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum(),
    df['moisturizer'].sum()
]

products = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.bar(products, total_sales)
plt.title("Total Sales per Product (Yearly)")
plt.ylabel("Total Units Sold")
plt.xticks(rotation=30)
plt.show()
