# retail_gui.py
# GUI-based Retail Transaction Insights using Tkinter

import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# ----------------------
# Load & Prepare Data
# ----------------------
file_path = 'Retail_Transactions_Dataset.csv'  # Change path if needed
df = pd.read_csv(file_path)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.day_name()

df['Total_Cost'] = pd.to_numeric(df['Total_Cost'], errors='coerce')
df['Total_Items'] = pd.to_numeric(df['Total_Items'], errors='coerce')

# ----------------------
# Create Main Window
# ----------------------
root = tk.Tk()
root.title("Retail Transaction Insights Dashboard")
root.geometry("900x700")  # Set window size

# ----------------------
# Top Stats Frame
# ----------------------
stats_frame = tk.Frame(root)
stats_frame.pack(pady=10)

total_transactions = df.shape[0]
unique_customers = df['Customer_Name'].nunique()
avg_spending = df.groupby('Customer_Category')['Total_Cost'].mean().sort_values(ascending=False)
top_cities = df['City'].value_counts().head(5)
season_revenue = df.groupby('Season')['Total_Cost'].sum().sort_values(ascending=False)

# Display basic stats
tk.Label(stats_frame, text=f"Total Transactions: {total_transactions}", font=("Arial", 12)).grid(row=0, column=0, padx=20)
tk.Label(stats_frame, text=f"Unique Customers: {unique_customers}", font=("Arial", 12)).grid(row=0, column=1, padx=20)
tk.Label(stats_frame, text=f"Top Spending Category: {avg_spending.idxmax()}", font=("Arial", 12)).grid(row=1, column=0, padx=20)
tk.Label(stats_frame, text=f"Season with Highest Revenue: {season_revenue.idxmax()}", font=("Arial", 12)).grid(row=1, column=1, padx=20)

# ----------------------
# Top Cities Table
# ----------------------
table_frame = tk.Frame(root)
table_frame.pack(pady=10)

tk.Label(table_frame, text="Top 5 Cities by Transactions", font=("Arial", 12, "bold")).pack()

tree = ttk.Treeview(table_frame)
tree['columns'] = ('City', 'Transactions')
tree.column('#0', width=0, stretch=tk.NO)
tree.heading('#0', text='', anchor=tk.W)
tree.column('City', anchor=tk.W, width=150)
tree.heading('City', text='City', anchor=tk.W)
tree.column('Transactions', anchor=tk.CENTER, width=100)
tree.heading('Transactions', text='Transactions', anchor=tk.CENTER)

for city, count in top_cities.items():
    tree.insert('', tk.END, values=(city, count))

tree.pack()

# ----------------------
# Matplotlib Plots Frame
# ----------------------
plot_frame = tk.Frame(root)
plot_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Plot 1: Transactions per City
fig1, ax1 = plt.subplots(figsize=(6,3))
df['City'].value_counts().plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_title("Transactions per City")
ax1.set_ylabel("Number of Transactions")
canvas1 = FigureCanvasTkAgg(fig1, master=plot_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(pady=10)

# Plot 2: Average Spending per Customer Category
fig2, ax2 = plt.subplots(figsize=(6,3))
avg_spending.plot(kind='bar', ax=ax2, color='lightgreen')
ax2.set_title("Average Spending per Customer Category")
ax2.set_ylabel("Average Total Cost")
canvas2 = FigureCanvasTkAgg(fig2, master=plot_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(pady=10)

# Plot 3: Monthly Revenue Trend
monthly_rev = df.groupby(df['Date'].dt.to_period('M'))['Total_Cost'].sum()
fig3, ax3 = plt.subplots(figsize=(6,3))
monthly_rev.plot(kind='line', ax=ax3, marker='o', color='orange')
ax3.set_title("Monthly Revenue Trend")
ax3.set_ylabel("Total Revenue")
ax3.set_xlabel("Month")
canvas3 = FigureCanvasTkAgg(fig3, master=plot_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(pady=10)

# ----------------------
# Run the GUI
# ----------------------
root.mainloop()